class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = None
        self.__balance = 0.0
        
        # Initialize values using setters
        self.set_account_number(account_number)
        self.set_balance(balance)

    # Public Setter Methods
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = float(balance)
        else:
            print("The balance must be not be a negative number.")

    # Public Getter Methods using @property decorator
    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance


# Demonstration / Object Creation matching sample output
if __name__ == "__main__":
    # Object of class BankAccount
    a1 = BankAccount(12345, 1000)

    print("Account 1")
    print(f"Account Number: {a1.account_number}")
    print(f"Balance: {a1.balance:.2f}\n")

    print("Update balance to -100")
    a1.set_balance(-100)

    print(f"Account Number: {a1.account_number}")
    print(f"Balance: {a1.balance:.2f}")