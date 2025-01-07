import math
import re
import sys
from datetime import date

import inflect

p = inflect.engine()


def main():
    user_input = input("Date of Birth: ")
    print(calculate_mins(user_input))


def calculate_mins(s):
    matches = re.search(r"^(\d{4})-([0-1]?[0-9])-([0-3]?[0-9])$", s)
    if matches:
        # Create user birthday from groups in regex match
        birth_year = matches.group(1)
        birth_month = matches.group(2)
        birth_day = matches.group(3)

        # Create birthday date object
        birthday_date = date(int(birth_year), int(birth_month), int(birth_day))

        # Get today's date object
        today = date.today()

        # Get difference and convert from seconds to minutes
        delta = math.trunc((today - birthday_date).total_seconds() / 60)
        return f"{p.number_to_words(delta, andword='').capitalize()} minutes"
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
