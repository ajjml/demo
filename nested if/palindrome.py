n = int(input('enter a number'))
t = n
rev = 0 
while n!=0:
    rem = n%10
    rev = rev*10+rem
    n//=10
if t == rev:
    print("it is palindrome")
else:
    print("not")

    

