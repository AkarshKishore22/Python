import numpy as np
global a
a=np.array([1,2,3,4,-1,-4,0])



def sum():
    global c
    c=0  
    for i in a:
        if i>0:
            c+=i

    return c
print(sum())