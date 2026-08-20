class BankAccount:

    bank_name = "ABC Bank"          # Public class attribute

    def __init__(self, owner, balance, pin):
        self.owner = owner          # Public attribute
        self._balance = balance     # Protected attribute
        self.__pin = pin            # Private attribute

    # Getter
    @property
    def balance(self):
        return self._balance

    # Setter
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative")
        else:
            self._balance = amount

    # Private method
    def __show_pin(self):
        print(f"PIN: {self.__pin}")

    # Public method
    def show_account(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")

    def check_pin(self, pin):
        if pin == self.__pin:
            print("Correct PIN")
            return True

        print("Wrong PIN")
        return False


# Create object
account = BankAccount("Sajib", 10000, 1234)

# Public attribute
print(account.owner)

# Protected attribute
print(account._balance)

# Private attribute
# print(account.__pin)       # Error

# Name mangling
print(account._BankAccount__pin)

# Getter
print(account.balance)

# Setter
account.balance = 15000
print(account.balance)

# Invalid value
account.balance = -500

# Public method
account.show_account()

# Private data through public method
account.check_pin(1234)
account.check_pin(9999)