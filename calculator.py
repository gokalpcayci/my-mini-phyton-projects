operations = ["+", "-", "*", "/"]


def calculator():
    continue_operation = True
    first_number = float(input("What's the first number: "))
    for operation in operations:
        print(operation)
    result = 0
    while continue_operation:
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number: "))

        if operation == "+":
            result = first_number + next_number
        elif operation == "-":
            result = first_number - next_number

        elif operation == "*":
            result = first_number * next_number

        elif operation == "/":
            result = first_number / next_number

        else:
            print("Invalid operation entered")
            continue
        print(f"{first_number} {operation} {next_number} = {result}")
        first_number = result
        continue_operation = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if continue_operation == "y":
            continue_operation = True
        if continue_operation == "n":
            continue_operation = False


calculator()
