-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Display the crime scene info from the crime_scene_reports table of crimes that took place on July 28th and on Humphrey St
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street LIKE 'Humphrey%';

-- Interviews were conducted on the same day as the crime report, get interviews from that day
SELECT * FROM interviews WHERE month = 7 AND day = 28 AND year = 2021;

-- Eugene mentions that he recognized the thief, it was someone who was using the ATM earlier that morning, check atm logs from that day before 10:15am on Leggett St. withdrawing money
SELECT * FROM atm_transactions WHERE month = 7 AND day = 28 AND year = 2021 AND atm_location LIKE 'Leggett%' AND transaction_type = 'withdraw';

-- Ruth says they saw within 10 min of the theft (10:15am) the thief leave in the car, check bakery surveillance to get license plate
SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND year = 2021 AND hour = 10 AND minute >= 15 AND activity = 'exit' AND minute <= 25;

-- Cross reference all of the license plates that left within that time with people
SELECT *
  FROM people
  JOIN (SELECT license_plate
    FROM bakery_security_logs
    WHERE month = 7 AND day = 28 AND year = 2021 AND hour = 10 AND minute >= 15 AND activity = 'exit' AND minute <= 25) as security_log
  ON security_log.license_plate = people.license_plate;

-- Get phone calls made that were less than or equal to a minute
SELECT * FROM phone_calls WHERE month = 7 AND day = 28 AND year = 2021 AND duration <= 60;

-- Combine the list of people leaving and the phone calls made on the same day around that time
SELECT * FROM people
  JOIN (SELECT license_plate
    FROM bakery_security_logs
    WHERE month = 7 AND day = 28 AND year = 2021 AND hour = 10 AND minute >= 15 AND activity = 'exit' AND minute <= 25) as security_log
    ON security_log.license_plate = people.license_plate
WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month = 7 AND day = 28 AND year = 2021 AND duration <= 60);

-- Get bank info from the list of people above
SELECT * FROM bank_accounts JOIN (
  SELECT * FROM people
  JOIN (SELECT license_plate
    FROM bakery_security_logs
    WHERE month = 7 AND day = 28 AND year = 2021 AND hour = 10 AND minute >= 15 AND activity = 'exit' AND minute <= 25) as security_log
    ON security_log.license_plate = people.license_plate
WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month = 7 AND day = 28 AND year = 2021 AND duration <= 60)
) as suspects
ON suspects.id = bank_accounts.person_id;

-- Search airports to get id for fiftyville
SELECT id FROM airports WHERE city LIKE 'Fifty%';

-- Search flights leaving the next day of the crime out of fiftyville and sort by earliest
SELECT id FROM flights
 WHERE month = 7 AND day = 29 AND year = 2021
 AND origin_airport_id = (SELECT id FROM airports WHERE city LIKE 'Fifty%')
 ORDER BY hour ASC
 LIMIT 1;

 -- Get passenger manifest for flight
 SELECT * FROM passengers WHERE flight_id = (
  SELECT id FROM flights
    WHERE month = 7 AND day = 29 AND year = 2021
    AND origin_airport_id = (SELECT id FROM airports WHERE city LIKE 'Fifty%')
    ORDER BY hour ASC
    LIMIT 1
 );

 -- Get Bruce's accomplice via the receiveing phone call (375) 555-8161
SELECT name FROM people WHERE phone_number = '(375) 555-8161';