##print('hi world')

x=[1,2,3,4,5,6,7,8,9]

y =[]

for i in range(len(x)):

    w = x[i]**3-x[i]**2-x[i]-1

    z = 1/ 1 + x[i]**2

    y.append(list(zip(w,z)))

print(y)


