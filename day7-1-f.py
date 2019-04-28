import numpy as np

M1 = np.array([
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1)]);
def is_perm_matrix(M) :
    for sumRow in np.sum(M, axis=1) :
        if sumRow != 1 :
            return False
    for sumCol in np.sum(M, axis=0) :
        if sumCol != 1 :
            return False
    return True

if is_perm_matrix(M1) == True:
    print ("given matrix is permutation matrix.")
else:
    print("given matrix is not a permitation matrix.")


