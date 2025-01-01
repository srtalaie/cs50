import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    if "to" not in s:
        raise (ValueError)
    search = re.search(
        r"^((?:[0-2]?[0-9])(?::)?(?:[0-5][0-9])?)\s(AM|PM)\sto\s((?:[0-2]?[0-9])(?::)?(?:[0-5][0-9])?)\s(AM|PM)?",
        s,
        re.IGNORECASE,
    )
    if search:
        begin_time, begin_meridiem, end_time, end_meridiem = search.groups()
        if check_mins(begin_time) or check_mins(end_time):
            if begin_meridiem == "AM" and end_meridiem == "AM":
                return f"{convert_AM_hours(begin_time)} to {convert_AM_hours(end_time)}"
            elif begin_meridiem == "AM" and end_meridiem == "PM":
                return f"{convert_AM_hours(begin_time)} to {convert_PM_hours(end_time)}"
            elif begin_meridiem == "PM" and end_meridiem == "PM":
                return f"{convert_PM_hours(begin_time)} to {convert_PM_hours(end_time)}"
            elif begin_meridiem == "PM" and end_meridiem == "AM":
                return f"{convert_PM_hours(begin_time)} to {convert_AM_hours(end_time)}"
            else:
                raise (ValueError)
        else:
            raise (ValueError)
    else:
        raise (ValueError)


def convert_AM_hours(s):
    if ":" in s:
        str_arr = s.split(":")
        str_hours = int(str_arr[0])
        if 1 <= str_hours <= 9:
            return f"{str_hours:02}:{str_arr[1]}"
        elif str_hours == 12:
            return f"00:{str_arr[1]}"
        else:
            return s
    else:
        s = int(s)
        if s == 12:
            return f"00:00"
        else:
            return f"{s:02}:00"


def convert_PM_hours(s):
    if ":" in s:
        str_arr = s.split(":")
        str_hours = int(str_arr[0]) + 12
        if str_hours == 24:
            return f"12:{str_arr[1]}"
        else:
            return f"{str_hours}:{str_arr[1]}"
    else:
        s = int(s) + 12
        if s == 24:
            return f"12:00"
        else:
            return f"{s}:00"


def check_mins(s):
    if ":" in s:
        str_arr = s.split(":")
        str_mins = int(str_arr[1])
        if 00 <= str_mins <= 59:
            return True
        else:
            return False
    else:
        return True


if __name__ == "__main__":
    main()
