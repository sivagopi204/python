import numpy
from numpy import array,poly,roots
A=array([[0.95, 0.03], [0.05, 0.97]])
ce = poly(A)
print(ce)
d= roots(ce)
print(d)
