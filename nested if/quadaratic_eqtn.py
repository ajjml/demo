a = int(input("enter the 1st number :"))
b = int(input("enter the 2nd number :"))
c = int(input("enter the 3rd number :"))
r = b**2-4*a*c
if r == 0:
    v1 = -b/(2*a)
    print(v1)
elif r>0:
    v2 = (-b + (r)**1/2)/(2*a)
    v3 = (-b - (r)**1/2)/(2*a)
    print(v2,v3)
else:
  print("no values")
