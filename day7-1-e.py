

def isOrthogonal(a, m, n) : 
	if (m != n) : 
		return False
	
	# Multiply A*A^t 
	for i in range(0, n) : 
		for j in range(0, n) : 
			sum = 0
			for k in range(0, n) : 
		
				# Since we are multiplying 
				# with transpose of itself. 
				# We use a[j][k] instead 
				# of a[k][j] 
				sum = sum + (a[i][k] *
							a[j][k]) 
		
		if (i == j and sum != 1) : 
			return False
		if (i != j and sum != 0) : 
			return False

	return True

# Driver Code 
a = [[1, 0, 0], 
	[0, 1, 0], 
	[0, 0, 1]] 
if (isOrthogonal(a, 3, 3)) : 
	print ("The given matrix is Orthogonal matrix") 
else : 
	print ("The given matrix is not an Orthodonal matrix") 
	
 
