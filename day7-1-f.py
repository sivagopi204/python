import itertools

def I(n):
    A = []
    for i in range(n):
        A.append([1 if j == i else 0 for j in range(n)])
    return A

#tests:

A = I(3)

for m in itertools.permutations(A):
    print('\n'.join(str(row) for row in m))
    print('')

