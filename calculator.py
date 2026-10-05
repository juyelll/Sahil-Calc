
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


def add_to_history(history, num1, num2, operation, result):
    history.append(f"{num1} {operation} {num2} = {result}")


def show_history(history):
    if not history:
        print("No calculations in history yet.")
        return

    print("\nCalculator History:")
    for index, entry in enumerate(history, start=1):
        print(f"{index}. {entry}")
    print()


def display_menu():
    print("=== SAHILCALC V1 ===")
    print("1. Perform a calculation")
    print("2. View history")
    print("3. Clear history")
    print("4. Exit")
    print()


def run_calculator():
    history = []

    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            print("A simple calculator made by Sahil")
            print()

            num1 = read_float("Enter the first number: ")
            num2 = read_float("Enter the second number: ")
            operation = read_operator()

            try:
                result = calculate(num1, num2, operation)
                add_to_history(history, num1, num2, operation, result)
                print("\nResult:", result)
            except (ZeroDivisionError, ValueError) as error:
                print(error)

        elif choice == "2":
            show_history(history)

        elif choice == "3":
            history.clear()
            print("History cleared.")

        elif choice == "4":
            print("Thank you for using SAHILCALC V1. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

        print()


def main():
    run_calculator()


if __name__ == "__main__":
    main()