def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))


def convert(fraction):
    formatted_string = fraction.split("/")

    x = int(formatted_string[0])
    y = int(formatted_string[1])

    if y >= x:
        percent = round((x / y) * 100)
        return percent
    elif y == 0:
        raise ZeroDivisionError
    else:
        raise ValueError


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
