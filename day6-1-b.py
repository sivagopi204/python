V=[-2,-1,-2]
modV=0
import math
for x in range(0,3):
    modV+=V[x]**2
modV=math.sqrt(modV)
for y in range(0,3):
    V[y]=V[y]/modV
print(V)
