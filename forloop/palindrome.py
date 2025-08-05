str=input("enter the string;")
rev=" "

for i in str:
    rev=i+rev
if rev==str:
    print("palindrome")
else:
    print("not")