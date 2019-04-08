
X = [[12,7,],
    [4 ,5,],
    [3 ,8,],
    [1, 6]]

def transpose1(mat):
    return list(list(row) for row in zip(*mat))


k=transpose1(X)
print("The first transpose of the matrix is:",k)
b=transpose1(k)
print("The second time of the transpose is:",b)
