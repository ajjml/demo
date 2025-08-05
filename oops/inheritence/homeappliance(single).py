class Appliance:
    def __init__(self,brand,power_rating):
        self.brand=brand
        self.power_rating=power_rating
        self.status='Off'
    
    def turn_on(self):
        self.status='On'
        print(self.brand,"Appliences now on")

    def turn_off(self):
        self.status='Off'
        print(self.status,"Appliencess now off") 

    def show_info(self):
        print("-------Appliences Detailes :--------\n")
        print("appliences brand :",self.brand,"\n")
        print("Applience power rating :",self.power_rating,'\n')
        print("Appliences Status :", self.status)


       
class WashingMachine(Appliance):
    def __init__(self,capacity,brand,power_rating):
        super().__init__(brand,power_rating)
        self.mode='Normal'
        self.capacity=capacity


    def set_mode(self,mode):
        self.mode=mode
        print("Wash mode set to",self.mode)
    def start_wash(self):
        if self.status=='On':
            print("Washing ",self.capacity,'kg load using',self.mode)
        else:
            print("we need to on the machine")

        
     


b=input('enter the brand : ')
p=input('enter the power rating : ')
c=input("enter the capacity :")
obj=WashingMachine(c,b,p)
i= 1
while(i):
    print("------Menu-------")
    print("1.Turn On")
    print("2.Turn OFF")
    print("3.Set Wash Mode")
    print("4.Start Washing")
    print("5.Show Appliance Info")
    print("6.Exit")

    choice=int(input("Enter your choice (1-6)"))

    if choice==1:
        obj.turn_on()
    elif choice==2:
        obj.turn_off()
    elif choice==3:
        x = input("enter the wash mode: ")
        obj.set_mode(x)
    elif choice==4:
        obj.start_wash()
    elif choice==5:
        obj.show_info()
    else:
        print("Exit....")
        i =0

    


# obj=Appliance(b,p)
# print(obj.show_info())
# print(obj.turn_off())
# print(obj.turn_on())

   