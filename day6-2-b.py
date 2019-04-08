# Python3 implementation for dot product 
# and cross product of two vector. 

n = 3

def sum_vectors(vect_A, vect_B):
    return [x[0] + x[1] for x in zip(vect_A, vect_B)]


def innerProduct(vect_A, vect_B): 

	product = 0

	for i in range(0, n): 
		product = product + vect_A[i] * vect_B[i] 

	return product

cross_P = []
def crossProduct(vect_A, vect_B): 
        
        cross_P.append(vect_A[1] * vect_B[2] - vect_A[2] * vect_B[1])
        cross_P.append(vect_A[0] * vect_B[2] - vect_A[2] * vect_B[0])
        cross_P.append(vect_A[0] * vect_B[1] - vect_A[1] * vect_B[0]) 


# Driver function 
if __name__=='__main__': 
	vect_A = [3, -5, 4] 
	vect_B = [2, 6, 5]
	
#addition function calling
	print("Addition of two vectors",end=" ")
	print(sum_vectors(vect_A,vect_B))
	
# dotProduct function call 
	print("Inner product:", end=" ") 
	print(innerProduct(vect_A, vect_B)) 

# crossProduct function call 
	print("Cross product:", end=" ") 
	crossProduct(vect_A, vect_B) 

# Loop that print 
# cross product of two vector array. 
	for i in range(0, n): 
		print(cross_P[i], end=" ") 


