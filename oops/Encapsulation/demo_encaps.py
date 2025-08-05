class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#'__' duel underscores gives it into make private

    def display(self):
        print('Name :',self.name , 'Age :',self.__age)

a=input("enter your Name")
b=int(input("Enter your age"))

obj=Student(a,b)
print(obj.display())