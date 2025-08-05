class Student:
    
   
    def display(self):
        print("\nName :",self.__name,"\nRoll no :",self.__rollno,)
           
    def set_student_details(self):
        name=input("Enter your Name :")
        rollno=int(input("Enter your Rollno :"))
        marks={}

        m=int(input("\nEnter math marks:"))
        marks['maths']=m
        s=int(input("\nenter science marks :"))
        marks['Sceince']=s
        e=int(input("\nenter english marks :"))
        marks['English']=e

        self.__name=name
        self.__rollno=rollno
        self.__marks=marks
    
    
    def calculate_average(self):
        self.add=sum(self.__marks.values())
        self.count=len(self.__marks)
        self.avg=self.add/self.count
        print(self.avg)

        
    def Average(self):
        if self.avg>=90:
            print('A')
        elif self.avg>=80 and self.avg<=89:
            print('B')
        elif self.avg>=70 and self.avg<=79:
            print('C')
        else:
            print('D')
        





obj=Student()
obj.set_student_details()
obj.display()
obj.calculate_average()
obj.Average()

