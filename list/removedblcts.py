# n=[1,2,3,4,5,4,6,3]
# li=[]

# for i in n:
#     if i in li:
#         li.append(i)
#     elif i in li:
#         break
# print(li)

l1=[]
l2=[]
for i in range(5):
    e=int(input('enter the elents'))
    l1.append(e)
for i in l1:
    if i not in l2:
        l2.append(i)
print('remove duplicate elements',l2)

