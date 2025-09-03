from operations import operations

def main(input_func=input, output_func=print):
    continue_flag = "YES"

    while continue_flag == "YES":
        output_func("--------------------------------")
        output_func("Account Management System")
        output_func("1. View Balance")
        output_func("2. Credit Account")
        output_func("3. Debit Account")
        output_func("4. Exit")
        output_func("--------------------------------")
        user_choice = input_func("Enter your choice (1-4): ")

        if user_choice == "1":
            operations("TOTAL")
        elif user_choice == "2":
            operations("CREDIT")
        elif user_choice == "3":
            operations("DEBIT")
        elif user_choice == "4":
            continue_flag = "NO"
        else:
            output_func("Invalid choice, please select 1-4.")

    output_func("Exiting the program. Goodbye!")


if __name__ == "__main__":
    main()