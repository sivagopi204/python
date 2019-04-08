X = [[1,1,1],
    [1 ,1,1],
    [1 ,1,1]]

# 3x4 matrix
Y = [[1,7,3],
    [4 ,5,6],
    [7 ,8,9]]


# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)
