#list of elemnts
# import numpy as np
# ary=np.array([1,2,3,4,5,6])
# print(type(ary))


#tupple of elements
# import numpy as np
# ary=np.array((1,2,3,4,5))
# print(type(ary))

# 2-d array
# import numpy as np
# ary=np.array([[1,2,3,4,4],[-1,2,7,6,4]])
# print(type(ary))

# 0-d array
# import numpy as np
# ary=np.array(4)
# print(type(ary))

#an array that has 0-d arrays as its elements is called uni-dimensional or 1-d array
# import numpy as np
# ary=np.array([1,2,3,4,5])
# print(type(ary))


# import numpy as np
# ary=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[3,4,5]]])
# print(type(ary))

import numpy as np
# ary=np.array(5)
# print(ary.ndim)



# ary=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[3,4,5]]])
# print(ary.ndim)

ary=np.array([[1,2,3,7],
             [2,3,4,9],
             [5,5,7,6],
             [8,9,7,2]])
ary2=ary[:3,::2]
print(ary2)