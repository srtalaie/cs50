from project import cap_gains_calc, income_calc, message_crafter

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


def test_income_calc():
    assert income_calc(100000, SINGLE_FILING) == 17052.66
    assert income_calc(200000, MARRIED_JOINTLY) == 34105.659999999996
    assert income_calc(55880, MARRIED_SEPARATELY) == 7346.26
    assert income_calc(30500, HEAD_OF_HOUSEHOLD) == 3328.88


def test_capital_gains_calc():
    assert cap_gains_calc(100) == 20.0


def test_message_crafter():
    str1 = message_crafter(
        100000,
        10000,
        14000,
        200,
        "Marital Status: Unmarried\nFiling: Individual, No Dependents",
    )
    str2 = "Marital Status: Unmarried\nFiling: Individual, No Dependents\nIncome: $100000.00\nCapital Gains: $10000.00\nTaxes on Income: $14000.00\nTaxes on Capital Gains: $200.00\nTotal Owed: $14200.00\n"
    assert str1.replace("\n", " ") == str2.replace("\n", " ")
