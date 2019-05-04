V=[2,1,2]
angles=[0,0,0,]
modV=0
import math
for x in range(0,3):
    modV+=V[x]**2
modV=math.sqrt(modV)
for y in range (0,3):
    angles[y]=math.degrees(math.acos(V[y]/modV))
for z in range(0,3):
    V[z]=math.cos(math.radians(angles[z]))
    print(V)
