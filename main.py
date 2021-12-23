import numpy as np
import matplotlib.pyplot as plt
import math
profile = np.genfromtxt("S3010.txt")
def gemoetricalMomentOfInertia(D): #IN MICROMETER!!
    #calculate to millimeter
    D = D*10**-3
    W = (math.pi*D**4)/64
    return W

def parallelAxesPortion(D,y):
    D = D*10**-3 #to millimeter
    R = D/2
    A = math.pi*R**2
    y = y*10**-3 #to millimerter
    PAP = abs(y**2)*A
    return PAP

def geometricCenterOfGravity(profile):
    return (sum(profile[:,1])/len(profile[:,1]))

def getMomentofInertia (profile,D,COG):
    gesMomentofInnertia = []
    gesMomentofBendingResistance = []

    for i in range(len(profile[:,0])):
        gesMom = gemoetricalMomentOfInertia(D)+parallelAxesPortion(D,profile[i,1])
        gesMomentofInnertia.append(gesMom)
        if abs(profile[i,1]) > 0 :
            W = gesMom/abs((profile[i,1]-COG)*10**-3)
            gesMomentofBendingResistance.append(W)

    return (gesMomentofInnertia,gesMomentofBendingResistance)

COG = geometricCenterOfGravity(profile)

I,W =  getMomentofInertia(profile,20,COG)


plt.plot(profile[:,0],profile[:,1])
plt.xlim(0,1)
plt.ylim(-.5,.5)
plt.text(0.1,0.3,"I = "+ str(round(sum(I),8))+" mm⁴",fontsize = 15)
plt.text(0.1,0.2,"W = "+ str(round(sum(W),8))+" mm³",fontsize = 15)
plt.xlabel("Meters")
plt.ylabel("Meters")
plt.show()