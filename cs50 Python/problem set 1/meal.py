def main():
    user_input = input("What time is it? ")
    formatted_time = convert(user_input)

    if 7.0 <= formatted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= formatted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= formatted_time <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.strip().split(":")
    minutes = float(minutes) / 60
    return float(hours) + minutes


if __name__ == "__main__":
    main()
