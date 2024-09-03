def print_menu():
    print("\nMenu options for arithmetic operations on two numbers:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def add(x, y):
    return x + y  # Addition of two numbers

def subtract(x, y):
    return x - y  # Difference of two numbers

def multiply(x, y):
    return x * y  # Multiplication of two numbers

def divide(x, y):
    if y == 0:  # Division of two numbers with zero-check
        return "Error! Division by zero."
    return x / y

def main():
    while True:
        try:
            # Prompt user for numeric values
            print("\n")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        print_menu()
        choice = input("Choose an operation (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Perform the selected operation
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
        else:
            print("Invalid choice. Please select a valid operation.")
            continue
        
        # Display the result
        print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
