import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

#print(a)
#print(a[:,1])

for r in a:
    print(r)


for r in a.flat:
    print(r)


a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)

print(a)
print(b)
print(np.hstack((a,b)))



