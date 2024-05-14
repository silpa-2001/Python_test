import datetime
class BankAccount:
    def __init__(self,acc,bal,dop,cn):
        self.acc=acc
        self.bal=bal
        self.dop=dop
        self.cn=cn

    
    def withdraw(self,amt):
        if self.bal>500:
            self.bal-=amt
            print("Sucessful withdrawal")
        else:
            print("Insufficient balance")
    def deposit(self,amt):
        self.bal+=amt
        print("Success")

    def chk_bal(self):
        print("Balance: "+str(self.bal))
c1=BankAccount(101,2000,'2021-12-23',"Ben")
c1.deposit(500)
c1.chk_bal()
c1.withdraw(200)
c1.chk_bal()

