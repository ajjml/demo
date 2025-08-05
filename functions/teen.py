# Check if a Person is a Teenager

def age(n):
    if n>=13 and n<=19 :
        return("you are a teenager")
    elif n>19 :
        return("you are a adult")
    else:
        return("you are a child")
a=int(input("enter your age"))
print(age(a))
    