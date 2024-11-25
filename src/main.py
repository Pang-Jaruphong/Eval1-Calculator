operand1 = None
operator = None
operand2 = None

def main():
    ask_user_input()
    result = calculate(operand1, operator, operand2)
    display_result(operand1, operator, operand2, result)

def ask_user_input():
    # Get first operand from the user
    global operand1
    operand1 = float(input("Enter the first operand: "))

    global operator
    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /): ")

    global operand2
    # Get second operand from the user
    operand2 = float(input("Enter the second operand: "))

def calculate(ope1, oper, ope2):
    # Perform the operation based on the operator
    match oper:
        case '+':
            res = ope1 + ope2
        case '-':
            res = ope2 - ope2
        case '*':
            res = ope1 * ope2
        case '/':
            if ope2 == 0:
                print("Error: Division by zero is undefined.")
                return
            res = ope1 / ope2
        case _:
            print("Invalid operator.")
            return
    return res


def display_result(op1, ope, ope2, res):
    print(float(op1) + " " + ope + " " + float(ope2) + " = " + float(res))


# Fonction puissance
def maFonction(n):
    somme = 1
    for count in range(int(n)):
        somme = somme * 2
    return somme

print(maFonction(3))
# Call the main function to run the program
main()