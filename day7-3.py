import numpy as np
A= np.array([[3,2,],[1,2]])
b = np.array([1,0])
z=np.linalg.solve(A,b)
print(z)

