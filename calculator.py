
def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter numeric values.")


def read_operator():
    while True:
        operation = input("Choose an operation: (+, -, *, /): ").strip()
        if operation in {"+", "-", "*", "/"}:
            return operation
        print("Invalid operation. Please choose from (+, -, *, /).")


def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Error: Division by zero is not allowed.")
        return num1 / num2
    raise ValueError("Invalid operation. Please choose from (+, -, *, /).")


def run_calculator():
    while True:
        print("=== SAHILCALC V1 ===")
        print()
        print("A simple calculator made by Sahil")
        print()

        num1 = read_float("Enter the first number: ")
        num2 = read_float("Enter the second number: ")
        print()
        print("First number:", num1)
        print("Second number:", num2)
        print()

        operation = read_operator()
        print()

        try:
            result = calculate(num1, num2, operation)
            print("Result:", result)
        except (ZeroDivisionError, ValueError) as error:
            print(error)

        print()
        calculate_again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()

        if calculate_again != "yes":
            print("Thank you for using SAHILCALC V1. Goodbye!")
            break

        print()


def main():
    run_calculator()


if __name__ == "__main__":
    main()