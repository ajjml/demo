#count of the number of vowels in a string

num=input("enter a number")
vowels="aeiouAEIOU"
count=0

for char in num :
    if char in vowels:
        count+=1
print("num in values:",count)
     
     