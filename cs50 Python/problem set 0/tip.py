def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    input = d.strip()
    cost = input.replace("$", "")
    return float(cost)


def percent_to_float(p):
    input = p.strip()
    tip_percent = input.replace("%", "")
    tip_percent = float(tip_percent) * 0.01
    return tip_percent


main()
