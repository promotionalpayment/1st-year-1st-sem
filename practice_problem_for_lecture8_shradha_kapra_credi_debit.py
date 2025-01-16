class Account:
    def __init__(self,bal,Acc_No):
        self.bal=bal
        self.Acc_no=Acc_No
    def debit_bal(self,debit):
        self.bal=self.bal-debit
        print("Your account has debited ",debit)
    def credit_bal(self,credit):
        self.bal=credit+self.bal
    def get_balance(self):
        print("Your remaining balance is ",self.bal)

s1=Account(10000,"456745351")
print("Accoutn no.      Balance")
print(s1.Acc_no,"    ",s1.bal)
debit=int(input("enter the amount you want to debit:"))
s1.debit_bal(debit)
s1.get_balance()
credit=int(input("enter the amount you want to credit:"))
s1.credit_bal(credit)
s1.get_balance()
