#  Create two lists of the same length and separate the odd numbers into the first list and even numbers into the second list without using a third list. Example:
# python
# Copy code
# Input:  a = [1, 2, 3],  b = [4, 5, 6]  
# # Output: a = [1, 3, 5],  b = [2, 4, 6]

def num(a,b):
    # a=[1,2,3] 
    # b=[4,5,6]
    for i in a:
        if i %2==0:
            b.append(i)
            a.remove(i)
    for i in b:
        if i %2!=0:
            a.append(i)
            b.remove(i)
    return a,b
a=[1,2,3] 
b=[4,5,6]
print(num(a,b))
    