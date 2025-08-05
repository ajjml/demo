s="ajmal"
l=len(s)
li=""
for i in range(l):
    if s[i] not in li:
        count = 1
        for j in range(i + 1, l):
            if s[j] == s[i]:
                count += 1
        li += s[i]
        print(s[i], count)


# s = input('enter the word ')
# count = 0
# li = ""

# for i in s:
#     if i not in li:
#         count = 0
#         for j in s:
#             if j == i:
#                 count += 1
#         print(i, count, "times")
#         # li+=i       
         
   