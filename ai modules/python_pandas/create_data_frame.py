import pandas as pd
import numpy as np


# a={
#     'data':[1,2,3],
#     'value':['one','two','three']
# }
# b=pd.DataFrame(a)
# print(b)

#Read the data in tuple

a=[(1,'ajmal',21),
   (2,'nibras',22),
   (3,'aftah',18)
   ]
b=pd.DataFrame(a,columns=['no','Name','age'])
# C=pd.Series(a)
# print(C.to_string(index=False))

#add the data in csv format
b.to_csv('new.csv',index=False)
c=pd.read_csv('new.csv')
print(c.to_string(index=False))