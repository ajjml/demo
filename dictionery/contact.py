contact={}
while True:
  print(1,'Add Contacts')
  print(2,'Edit Contact')
  print(3,'Delete Contact')
  print(4,'Display Contact')
  print(5,'Exit')
  a=int(input("enter your choice :"))
  if  a==1:
    name = (input("enter your name "))
    number = int(input("enter your ph num "))
    contact[name]= number
    print(name,"contact was addes successfully ")
  elif a==2:
    name = (input("enter th name to edit contact "))
    if name in contact:
      newnumber = int(input("enter the new number "))
      contact[name] = newnumber
      print(name,"updated successfully.")
    else:
      print("contact not found")
  elif a==3:
    name =(input("delete contact "))
    if name in contact:
     del contact[name] 
     print(name,"deleted successfully")
    else:
     print("contact not found")
   
  elif a==4:
    if contact:
     for name,number in contact.items():
       print(name,':',number)
     # print('hjdjdj':
    else:
       print("No conatcts")   
  else:
   print("exit")
    
 