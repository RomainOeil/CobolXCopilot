# Global variable to simulate the storage of the account balance
storage_balance = 1000.00

def read_balance():
    """
    Reads the current balance from storage.
    :return: The current balance as a float.
    """
    global storage_balance
    return storage_balance

def write_balance(new_balance):
    """
    Updates the balance in storage.
    :param new_balance: The new balance to be stored.
    """
    global storage_balance
    storage_balance = new_balance