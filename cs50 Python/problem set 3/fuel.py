while True:
    try:
        user_input = input("Fraction: ")
        formatted_string = user_input.split("/")

        x = int(formatted_string[0])
        y = int(formatted_string[1])

        if y >= x:
            percent = round((x / y) * 100)
            break

    except (ValueError, ZeroDivisionError):
        pass

if percent >= 99:
    print("F")
elif percent <= 1:
    print("E")
else:
    print(f"{percent}%")
