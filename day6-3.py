def cross_product(a, b):
     assert len(a) == len(b) == 3, 'Vectors a, b must be three-dimensional'
     return [a[1]*b[2] - a[2]*b[1],
             a[2]*b[0] - a[0]*b[2],
             a[0]*b[1] - a[1]*b[0]]

c_product=cross_product([1, 2, -1], [2, 0, -1])
print (c_product)
