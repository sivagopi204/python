import math
import numpy as np

vect_A = [3, -5, 4] 
vect_B = [2, 6, 5]
n=len(vect_A)	
def innerProduct(vect_A, vect_B): 

	product = 0

	for i in range(0, n): 
		product = product + vect_A[i] * vect_B[i] 

	return product
    
def angle(v1, v2):
    angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
    return angle

in_pro=innerProduct(vect_A,vect_B)
angle_vec=angle(vect_A,vect_B)
print ("The inner product of two vectors are:", in_pro)
print ("The angle between the two vectors is:", angle_vec)
