import numpy as np
import math
from scipy.constants import sigma
import matplotlib.pyplot as plt

proportion = np.zeros(49)
for iteration in range(1,50):
    rangemass=iteration*100
    #rangemass = 1000 #Amount of intervals I have for mass
    maxmass = 50.
    minmass = 5.

    bins = np.array(range(rangemass))
    masslabel = bins.astype(float)
    massintegral = np.array(range(rangemass))
    massintegral = massintegral.astype(float)

    def IMF(mass):
        e= 1/(1.3) * 1/(minmass**-1.3 - maxmass**-1.3)
        massfactor =  math.log(10)*e*mass**(-1.35)
        return massfactor

    for mass in range(0,rangemass):
        masss = 5*10**((float(mass))/rangemass)
        masslabel[mass]=IMF(masss)
        if mass==0:
            massintegral[mass]=IMF(masss)
        else:
            massintegral[mass]=massintegral[mass-1]+IMF(masss)

    proportion[iteration-1]=massintegral[rangemass-1]/rangemass

"""plt.plot(bins, massintegral)
plt.xlabel('bin')
plt.ylabel('integral of mass')
plt.show()"""
