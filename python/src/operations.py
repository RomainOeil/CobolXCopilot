from data import read_balance, write_balance

def operations(operation_type):
    if operation_type == "TOTAL":
        # View the current balance
        balance = read_balance()
        print(f"Current Balance: {balance:.2f}")

    elif operation_type == "CREDIT":
        # Credit the account
        try:
            credit_amount = float(input("Enter the amount to credit: "))
            balance = read_balance()
            new_balance = balance + abs(credit_amount)
            write_balance(new_balance)
            print(f"Account credited successfully. New Balance: {new_balance:.2f}")
        except ValueError:
            print(f"Account credited successfully. New Balance: {read_balance():.2f}")

    elif operation_type == "DEBIT":
        # Debit the account
        try:
            debit_amount = float(input("Enter the amount to debit: "))
            balance = read_balance()
            if abs(debit_amount) <= balance:
                new_balance = balance - abs(debit_amount)
                write_balance(new_balance)
                print(f"Account debited successfully. New Balance: {new_balance:.2f}")
            else:
                print("Insufficient funds. Debit amount exceeds current balance.")
        except ValueError:
            print(f"Account debited successfully. New Balance: {read_balance():.2f}")

    else:
        print("Invalid operation type.")