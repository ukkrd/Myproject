'''1.  In an array N1-N2 numbers are stored, one number is missing,
find the missing number.For example N1=1 and N2=10 1,2,3,4,6,7,8,9,10.
Answer -> 5'''

import numpy as np
a=np.array([1,2,3,4,6,7,8,9,10])
n=0
m=0
for i in range(1,11):
    n +=i
for i in a:
    m +=i
print("missing number is: {}".format(n-m))
