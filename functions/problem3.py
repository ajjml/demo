# Count the frequency of each element in a list without using any built-in functions like count() or collections.Counter.
def num(*n):
    a=[]
    # count=1
    for i in range(len(n)):
        # a.append(n[i])
        if n[i]  not in a:
            count=0
            for j in range(len(n)):
                if n[i] == n[j]:
                    count+=1
            a.append(n[i])
            print(n[i]," occurs ",count, "times")
num(1,2,3,4,5,6,3,4,2,1,5)
