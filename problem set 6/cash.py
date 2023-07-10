from cs50 import get_float


def main():
    cents = round(get_cents() * 100)

    # Calculate amount of quarters
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # Calculate amount of dimes
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate amount of nickels
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate amount of pennies
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    coins = quarters + dimes + nickels + pennies
    print(coins)


def get_cents():
  while True:
      try:
          cents = get_float("How much change is owed (in cents): ")
          if cents > 0:
              break
      except:
          print("Please input a valid amount")
  return cents


def calculate_quarters(cents):
    count = 0
    while (cents >= 25):
        cents = cents - 25
        count += 1
    return count


def calculate_dimes(cents):
    count = 0
    while (cents >= 10):
        cents = cents - 10
        count += 1
    return count


def calculate_nickels(cents):
    count = 0
    while (cents >= 5):
        cents = cents - 5
        count += 1
    return count


def calculate_pennies(cents):
    count = 0
    while (cents >= 1):
        cents = cents - 1
        count += 1
    return count


main()