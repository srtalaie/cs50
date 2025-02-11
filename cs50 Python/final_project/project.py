import argparse
import sys

# Brackets if filing as Single
SINGLE_FILING = [
    {"rate": 0.10, "lower_bound": 0.0, "upper_bound": 11600.0},
    {"rate": 0.12, "lower_bound": 11601.0, "upper_bound": 47150.0},
    {"rate": 0.22, "lower_bound": 47151.0, "upper_bound": 100525.0},
    {"rate": 0.24, "lower_bound": 100526.0, "upper_bound": 191950.0},
    {"rate": 0.32, "lower_bound": 191951.0, "upper_bound": 243725.0},
    {"rate": 0.35, "lower_bound": 243726.0, "upper_bound": 609350.0},
    {"rate": 0.37, "lower_bound": 609351.0},
]

# Bracket if filing Separatley but Marital Status is married
MARRIED_SEPARATELY = [
    {"rate": 0.10, "lower_bound": 0.0, "upper_bound": 11600.0},
    {"rate": 0.12, "lower_bound": 11601.0, "upper_bound": 47150.0},
    {"rate": 0.22, "lower_bound": 47151.0, "upper_bound": 100525.0},
    {"rate": 0.24, "lower_bound": 100526.0, "upper_bound": 191950.0},
    {"rate": 0.32, "lower_bound": 191951.0, "upper_bound": 243725.0},
    {"rate": 0.35, "lower_bound": 243726.0, "upper_bound": 365600.0},
    {"rate": 0.37, "lower_bound": 365601.0},
]

# Bracket if filing Jointly with Married Partner (combine both incomes)
MARRIED_JOINTLY = [
    {"rate": 0.10, "lower_bound": 0.0, "upper_bound": 23200.0},
    {"rate": 0.12, "lower_bound": 23201.0, "upper_bound": 94300.0},
    {"rate": 0.22, "lower_bound": 94301.0, "upper_bound": 201050.0},
    {"rate": 0.24, "lower_bound": 201051.0, "upper_bound": 383900.0},
    {"rate": 0.32, "lower_bound": 383901.0, "upper_bound": 487450.0},
    {"rate": 0.35, "lower_bound": 487451.0, "upper_bound": 731200.0},
    {"rate": 0.37, "lower_bound": 731201.0},
]

# Bracket if filing as Head of Household
HEAD_OF_HOUSEHOLD = [
    {"rate": 0.10, "lower_bound": 0.0, "upper_bound": 16550.0},
    {"rate": 0.12, "lower_bound": 16551.0, "upper_bound": 63100.0},
    {"rate": 0.22, "lower_bound": 63101.0, "upper_bound": 100500.0},
    {"rate": 0.24, "lower_bound": 100501.0, "upper_bound": 191950.0},
    {"rate": 0.32, "lower_bound": 191951.0, "upper_bound": 243700.0},
    {"rate": 0.35, "lower_bound": 243701.0, "upper_bound": 609350.0},
    {"rate": 0.37, "lower_bound": 609351.0},
]

parser = argparse.ArgumentParser(description="Income Tax Calculator")
parser.add_argument(
    "-ms",
    "--married_separate",
    help="Indicate if you are married",
    action="store_true",
)
parser.add_argument(
    "-mj",
    "--married_joint",
    help="Indicate if you are filing jointly",
    action="store_true",
)
parser.add_argument(
    "-hh",
    "--head_of_household",
    help="Indicate if you are filing as head of a household",
    action="store_true",
)
parser.add_argument(
    "-i",
    "--income",
    default=0.0,
    help="Income, either alone or combined if joint filing",
    type=float,
    required=True,
)
parser.add_argument(
    "-c",
    "--capital_gains",
    default=0.0,
    help="How much money you made through investments this year",
    type=float,
    required=False,
)


def main():
    args = parser.parse_args()
    """Calculate User Provided Tax Burden"""
    while True:
        try:
            filing = []
            status = ""
            if args.married_joint:
                status = "Marital Status: Married\nFiling: Jointly"
                filing = MARRIED_JOINTLY
            elif args.married_separate:
                status = "Marital Status: Married\nFiling: Separately"
                filing = MARRIED_SEPARATELY
            elif args.head_of_household:
                status = "Marital Status: Unmarried \nFiling: Having Dependents"
                filing = HEAD_OF_HOUSEHOLD
            else:
                status = "Marital Status: Unmarried\nFiling: Individual, No Dependents"
                filing = SINGLE_FILING

            income_owed = income_calc(args.income, filing)
            cap_gains_owed = cap_gains_calc(args.capital_gains)
            print(
                message_crafter(
                    args.income, args.capital_gains, income_owed, cap_gains_owed, status
                )
            )
            break
        except ValueError:
            sys.exit("Please provide a valid dollar amount as income.")
        except EOFError:
            sys.exit()
        except ZeroDivisionError:
            sys.exit("Something went wrong :(")


# Calculate Tax Owed on Income
def income_calc(income: float, filing: list) -> float:
    """
    Calculate taxes owed on income based on status

    :param income: Income made, if married and filing jointly combined income
    :type income: float
    :param filing: List of dicionaries, each containing tax brackets: rate at the bracket and the upper and lower bounds of the bracket
    :type filing: list
    :param status: Message provided describing marital status and filing status
    :type status: str
    :raise TypeError: Error raised if income is not a float, filing is not a list, or status is not a string
    :return: float of total owed on income tax
    :rtype: float
    """
    total_owed = 0.0
    try:
        for i in range(len(filing)):
            # Catch highest bracket
            if "upper_bound" not in filing[i]:
                if filing[i]["lower_bound"] < income:
                    tax_amount = (income - filing[i]["lower_bound"]) * filing[i]["rate"]
                    total_owed += tax_amount
            else:
                if filing[i]["upper_bound"] < income:
                    taxable_amount = filing[i]["upper_bound"] - filing[i]["lower_bound"]
                    tax_amount = taxable_amount * filing[i]["rate"]
                    total_owed += tax_amount
                elif filing[i]["lower_bound"] < income < filing[i]["upper_bound"]:
                    tax_amount = (income - filing[i]["lower_bound"]) * filing[i]["rate"]
                    total_owed += tax_amount
        return total_owed
    except TypeError:
        print("Please provide a valid value")


# Calculate amount owed on capital gains
def cap_gains_calc(capital_gains: float) -> float:
    """
    Calculate taxes owed on capital gains

    :param capital_gains: Capital gains earned on the year
    :type capital_gains: float
    :raise TypeError: Error raised if capital_gains is not a float
    :return: float of total owed on capital gains tax
    :rtype: float
    """
    return capital_gains * 0.20


# Returns message staing what the user owes
def message_crafter(
    income: float,
    cap_gains: float,
    income_owed: float,
    cap_gains_owed: float,
    status: str,
) -> str:
    """
    Calculate the total owed in taxes and create the message the console will display to users of how much is owed

    :param income: Income made, if married and filing jointly combined income
    :type income: float
    :param cap_gains: Capital gains earned on the year
    :type cap_gains: float
    :param income_owed: Taxes owed on income
    :type income_owed: float
    :param cap_gains_owed: Taxes owed on capital gains
    :type cap_gains_owed: float
    :param status: Message provided describing marital status and filing status
    :type status: str
    :raise TypeError: Error raised if income, cpa_gains, income_owed or cap_gains_owed are not a float, or status is not a string
    :return: Message of what the user owes on the year, including income and capital gains made as well as filing and marital ststus
    :rtype: str
    """
    total_owed = income_owed + cap_gains_owed
    return f"{status}\nIncome: ${income:.2f}\nCapital Gains: ${cap_gains:.2f}\nTaxes on Income: ${income_owed:.2f}\nTaxes on Capital Gains: ${cap_gains_owed:.2f}\nTotal Owed: ${total_owed:.2f}\n"


if __name__ == "__main__":
    main()
