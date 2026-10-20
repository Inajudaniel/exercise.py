def calculator():
    print("===== SIMPLE CLI CALCULATOR =====")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Exit the calculator
        if choice == "5":
            print("Thank you for using the calculator. Goodbye!")
            break

        # Check for invalid choices
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please choose between 1 and 5.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")

            elif choice == "2":
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")

            elif choice == "3":
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")

            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")


calculator()