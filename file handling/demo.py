
def file():
    
    a=int(input("enter the no of students : "))
    f=open('std.txt','w')
    for i in range(a):
            print('Enter th details of ',i+1,'th student')
            Name=input('enter your name :')
            Age=int(input('enter your age :'))
            Address=input("enter your address :")
            print("...................................")
            f.write(f"Name = {Name}\n")
            f.write(f"Age = {Age}\n")
            f.write(f"Address = {Address}\n")
            f.write('--------------------------------------------------------------\n')
            print("students details added successfully")
    f.close()


file()
