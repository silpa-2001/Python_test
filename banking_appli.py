import datetime

class Account:
    def __init__(self, acc, bal, dop, custname):
        self.acc = acc  # Account number
        self.bal = bal  # Balance
        self.dop = datetime.datetime.strptime(dop, '%Y-%m-%d').date()  # Date of opening (converted to datetime.date)
        self.custname = custname    # Account holder's name

    def deposit(self, amt):
        self.bal += amt
        print("Deposit successful")

    def withdraw(self, amt):
        raise NotImplementedError("Withdraw method not implemented")


    def check_balance(self):
        print(f"Account Number: {self.acc}")
        print(f"Account Holder: {self.custname}")
        print(f"Balance: {self.bal}")


class BankAccount(Account):
    def __init__(self, acc, bal, dop, custname):
        super().__init__(acc, bal, dop, custname)

    def withdraw(self, amt):
        if self.bal > 500:  # Ensure minimum balance of 500 is maintained
            if self.bal >= amt:
                self.bal -= amt
                print("Successful withdrawal")
            else:
                print("Insufficient balance")
        else:
            print("Minimum balance of 500 required. Cannot withdraw.")

# Example usage
c1 = BankAccount(101, 2000, '2021-12-23', "Ben")

# Deposit and check balance
print("The account is created on: ",c1.dop)
c1.deposit(500)
c1.check_balance()

# Withdraw and check balance
c1.withdraw(200)
c1.check_balance()
