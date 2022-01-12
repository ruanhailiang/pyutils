import numpy as np

a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
b = np.array([11,22,33])
print(a.shape)
print(b.shape)

c = np.vstack((a,b))
print(c)
d = np.column_stack((a,b))

print(d)