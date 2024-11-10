expression = input("Expression: ")

# Split expression and assign to variables. Cast integer variables to ints
x, y, z = expression.strip().split(" ")


def math_inerpreter(first_num, operator, second_num):
    match operator:
        case "+":
            return float(first_num) + float(second_num)
        case "-":
            return float(first_num) - float(second_num)
        case "*":
            return float(first_num) * float(second_num)
        case "/":
            return float(first_num) / float(second_num)


print(math_inerpreter(x, y, z))
