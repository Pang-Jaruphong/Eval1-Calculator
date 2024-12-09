from src.MathRequest import MathRequest
def main():
    math_request = ask_user_input()
    math_request.set_res(calculate(math_request))
    display_result(math_request)

def ask_user_input() -> MathRequest:
    # Get first operand from the user
    ope1 = ask_user_float_input("Enter the first operand: ")

    # Get the operator from the user
    oper = input("Enter an operator (+, -, *, /, ^): ")

    # Get second operand from the user
    ope2 = ask_user_float_input("Enter the second operand: ")

    return MathRequest(ope1, oper, ope2)

def ask_user_float_input(msg):
    return float(input(msg))

def calculate(math_request):
    # Perform the operation based on the operator
    ope1 = math_request.get_ope1()
    oper = math_request.get_oper()
    ope2 = math_request.get_ope2()

    match oper:
        case '+':
            res = ope1 + ope2
        case '-':
            res = ope1 - ope2
        case '*':
            res = ope1 * ope2
        case '/':
            if ope2 == 0:
                print("Error: Division by zero is undefined.")
                return
            res = ope1 / ope2
        case '^':
            res = 1
            for count in range(int(ope1)):
                res = res * ope2
        case _:
            print("Invalid operator.")
            return
    return res

def display_result(math_request):
    # Print the result
        print(math_request.to_string())


# Call the main function to run the program
main()