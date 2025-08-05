# #  Create an integer list and separate the prime and non-prime numbers into two different lists.
# def num(n):
#     a=[]
#     b=[]
#     c=[]
#     count=0
#     for i in range(n):
#         a.append(int(input()))
#     for j in a:
#         count=0
#         for k in range(1,j+1):
#             if j % k == 0:
#                 count+=1
#             if count == 2:
#                 b.append(j)
#             else:
#                 c.append(j)

#     print("prime numbers are: ", b, "non prime numbers are: ", c,) 



def primelist(a):
    prime=[]
    nonprime=[]
    for i in a:
        if i<2:
            nonprime.append(i)
        else:
            for j in range(2, i):
                if i%j==0:
                    nonprime.append(i)
                    break
            else:
                prime.append(i)
    print("Prime numbers:", prime)
    print("Non-prime numbers:", nonprime)

a=[1,2,3,4,5,6,7,8,9,10,25,14,45,89]
primelist(a)