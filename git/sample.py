from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass

    def transaction_summery(self):
        pass
       
class creditcardpayement(payment):
    def process_payment(self):
        name=input("\nenter the user name :")
        amount=int(input("\nenter the amount :"))
        cardno=input("\nenter your card no :")

        print('\n',name,'paid',amount,'using credit card ending with',cardno[8:])
        print(".....Transaction Successfull.....\n")

     
class UPIpayment(payment):
   
    def process_payment(self):
        name=input("\nEnter your Name :")
        amount=int(input("\nEnter the amount :"))
        UPIid=input("\nEnter your UPIid")
        print('\n',name,'attempted to pay',amount,'via UPI',UPIid)
        if amount>5000:
            print("Transaction Failed : Limit exceeded...")
        else:
            print("Transaction Successfull by ",UPIid)
            
i=True
while i:
    
    print(1,"Credit Card Payement\n")
    print(2,"UPIpayment\n")
    print("-----------------------------------")
    a=int(input("\nEnter Your Choice :"))

    if a==1:
        obj=creditcardpayement()
        obj.process_payment()
        break
    elif a==2:
        obj=UPIpayment()
        obj.process_payment()
        break
