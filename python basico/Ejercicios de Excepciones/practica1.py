def get_number(message):
    while True:
        user_input = input(message)
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid number.")


def multiply(current_number, second_number):
    return current_number * second_number


def divide(current_number, second_number):
    if second_number == 0:
        print("You cannot divide by zero.")
        return current_number
    return current_number / second_number


def add(current_number, second_number):
    return current_number + second_number


def subtract(current_number, second_number):
    return current_number - second_number


def clear_result():
    return get_number("Enter a new current number: ")


def show_menu(current_number):
    print("\nCurrent number:", current_number)
    print("1. Multiply")
    print("2. Divide")
    print("3. Add")
    print("4. Subtract")
    print("5. Clear result")
    print("6. Exit")


def main():
    current_number = get_number("Enter the initial number: ")

    while True:
        show_menu(current_number)
        option = input("Choose an option: ")

        if option == "1":
            second_number = get_number("Enter the second number: ")
            current_number = multiply(current_number, second_number)
            print("Result:", current_number)

        elif option == "2":
            second_number = get_number("Enter the second number: ")
            current_number = divide(current_number, second_number)
            print("Result:", current_number)

        elif option == "3":
            second_number = get_number("Enter the second number: ")
            current_number = add(current_number, second_number)
            print("Result:", current_number)

        elif option == "4":
            second_number = get_number("Enter the second number: ")
            current_number = subtract(current_number, second_number)
            print("Result:", current_number)

        elif option == "5":
            current_number = clear_result()
            print("The result has been cleared.")
            print("New current number:", current_number)

        elif option == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a valid menu option.")


main()