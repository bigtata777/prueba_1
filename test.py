##print('hi world')

import math as mt

import numpy as np

#x=[1,2,3,4,5,6,7,8,9,10,11,12]

x = np.linspace(0,10,num=20)

y =[]

for i in range(len(x)):

    w = mt.sqrt((x[i]**3 + x[i]**2 + x[i] +1)/(1+x[i]**2 - 0.008*x[i]))
    
    z = (w)

    y.append(z)

print(y)
print(sum(y))

