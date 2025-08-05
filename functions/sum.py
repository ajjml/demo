# Check if the Sum of Two Numbers is Even

def num(n1,n2):
    s=n1+n2
    if s%2==0:
        return("it is even")
    else:
        return("it is not")
n1=int(input("enter a number"))
n2=int(input("enter a number"))
print(num(n1,n2))
    