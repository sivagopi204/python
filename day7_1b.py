
m=[[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]

def sum_of_diags(matrix):
    size = len(matrix[0])
    if size == 1:
        return matrix[0][0]*2
    diag_sum = 0

    for i in range(size):
        diag_sum += matrix[i][i]
        #diag_sum += matrix[i][size-i-1]
    return diag_sum

k=sum_of_diags(m)
print("The Trace of the matrix %s is:"%m,k)
