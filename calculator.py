while True:
    print("=== SAHILCALC V1 ===")
    print()

    try:
        print("A simple calculator made by Sahil")
        print()
        print("Enter the first number:")
        num1 = float(input())
        print()
        print("Enter the second number:")
        num2 = float(input())
        print()
        print("First number:", num1)
        print("Second number:", num2)
        print()

        print("Choose an operation: (+, -, *, /)")
        operation = input()
        print()

        if operation == "+":
            result = num1 + num2
            print("Result:", result)
        elif operation == "-":
            result = num1 - num2
            print("Result:", result)
        elif operation == "*":
            result = num1 * num2
            print("Result:", result)
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print("Result:", result)
        else:
            print("Invalid operation. Please choose from (+, -, *, /).")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception:
        print("An error occurred:")

    print("Do you want to perform another calculation? (yes/no): ")
    calculate_again = input().strip().lower()

    if calculate_again == "yes":
        continue

    print("Thank you for using SAHILCALC V1. Goodbye!")
    break