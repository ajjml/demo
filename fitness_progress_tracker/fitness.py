class school:
    def __init__(self,studentname,studentclass):
        self.n1=studentname
        self.c1=studentclass


    def display(self):
        print("-----Student Details-----")
        print("\nStudent Name :",self.n1)
        print("\nStudent Class :",self.c1)        

a=input("Enter Your Name : ")
b=input("Choose Your Stream :")
obj=school(a,b)
print(obj.display)