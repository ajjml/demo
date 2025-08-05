class Atm:
    def __init__(self,AccountHolder,Accountno,balance=0):
        self.a1=AccountHolder
        self.a2=Accountno
        self.b1=balance

    def display(self):
        print('.....Account Detailes.....')
        print('\nAccount Holder :',self.a1)
        print('\nAccount number :',self.a2)

    def deposit(self):
        dpst=int(input("enter the Amount"))
        self.b1+=dpst

    def Withdraw(self):
        wthdrw=int(input('enter the Withdraw Amount'))
        if wthdrw>self.b1:
            print("insuffient balance")
        else:
            self.b1-=wthdrw
    
    def view(self):
        print(self.b1)


n=input('enter your account name')
a=int(input("enter you account nmbr"))

obj=Atm(n,a)
print(obj.display())

while True:
    print(1,'Deposit Money')
    print(2,'Withdraw Money')
    print(3,'View Balance')
    print(4,'exit')
    a=int(input("Enter Your Choice"))

    if a==1:
        obj.deposit()
    elif a==2:
        obj.Withdraw()
    elif a==3:
        obj.view()
    else:
        print("EXITING...........")
        break