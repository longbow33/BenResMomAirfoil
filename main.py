import numpy as np
import matplotlib.pyplot as plt
import math
profile = np.genfromtxt("NACA0012.txt")

def gemoetricalMomentOfInnertia(D): #IN MICROMETER EINGEBEN!!
    #umrechnen nach micrometer
    D = D*10**-6
    W = (math.pi*D**4)/64
    return W

def parallelAxesPortion(D,y):
    R = D/2
    A = math.pi*R**2
    PAP = (y**2)*A
    return PAP

def getMomentofInnertia (profile,D):
    gesMomentofInnertia = []
    gesMomentofBendingResistance = []

    for i in range(len(profile[:,0])):
        gesMom = gemoetricalMomentOfInnertia(D)+parallelAxesPortion(D,profile[i,1])
        gesMomentofInnertia.append(gesMom)
        if profile[i,1] > 0 :
            W = gesMom/profile[i,1]
            print(W)
            gesMomentofBendingResistance.append(W)

    return (gesMomentofInnertia,gesMomentofBendingResistance)


I,W =  getMomentofInnertia(profile,20)


plt.plot(profile[:,0],profile[:,1])
plt.xlim(0,1)
plt.ylim(-.5,.5)
plt.text(0.1,0.3,"Flächenträgheitsmoment = "+ str(round(sum(I,2)))+" m⁴",fontsize = 15)
plt.text(0.1,0.2,"Biegewiderstandsmoment = "+ str(round(sum(W,2)))+" m³",fontsize = 15)
plt.show()