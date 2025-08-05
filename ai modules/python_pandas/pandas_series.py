import pandas as pd
import numpy as np

#create an array
a=np.array([1,2,3])

#create an series
b=pd.Series(a,index=['name','age','place'])
# r=pd.Series(a)
print(b)