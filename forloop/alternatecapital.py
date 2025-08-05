a=input("enter a num")
word=''

for i in a :
   word+=i
   if len(word)%2==0:
      print(i.lower(),end='')
   else:
      print(i.upper(),end='')
      
#input=ajmal
#output=AjMaL