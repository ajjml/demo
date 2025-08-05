# def file():
import matplotlib.pyplot as plt

    # a=int(input("enter the no of students :"))
    # f=open('std.txt','w')
    # for i in range(a):
        # print('enter the details of ',i+1,'th student')
Rollno= int(input("Enter your Roll number: "))
Name =input("enter your Name")
    
        # print("................................")
plt.plot(Rollno,Name,c='Red')    
plt.xlabel(f"Rollno = {Rollno}")
plt.ylabel(f"Name = {Name}") 
plt.show()

        
        # print("added")
    # f.close()

# print(file())