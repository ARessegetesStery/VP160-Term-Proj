import math
import numpy

# This file includes the functions needed for problem 4.2

# Using the analytical method we have learnt in class to calculate
def getAnalyticalList(steps):
    deltaT = 10 / steps # We take ten seconds as the time interval, following are the same.
    xListAnalytical = []
    vxListAnalytical = []
    eListAnalytical = []
    time = []
    for i in range(0, steps):
        xtemp = 5 / 6 * math.cos(1.5 * i * deltaT - numpy.arccos(0.6))
        xListAnalytical.append(xtemp)
        vxtemp = -5 / 6 * 1.5 * math.sin(1.5 * i * deltaT - numpy.arccos(0.6))
        vxListAnalytical.append(vxtemp)
        eListAnalytical.append(1/2 * (1.5 * 1.5 * xtemp * xtemp + vxtemp * vxtemp))
        time.append(i * 10 / steps)
    return (xListAnalytical, vxListAnalytical, eListAnalytical, time)

# Using the Euler's method to calculate
def getEulerList(steps):
    deltaT = 10 / steps
    vxListEuler = [1] # The first step
    xListEuler = [0.5]
    eListEuler = [25/32]
    time = [0]
    for i in range(1, steps):
        vxtemp = vxListEuler[i - 1] - (1.5 * 1.5 * xListEuler[i - 1] * deltaT)
        vxListEuler.append(vxtemp)
        xtemp = xListEuler[i - 1] + vxListEuler[i - 1] * deltaT
        xListEuler.append(xtemp)
        eListEuler.append(1/2 * (1.5 * 1.5 * xtemp * xtemp + vxtemp * vxtemp)) # When calculating energy, we take the mass to be 1kg, following are the same
        time.append(i * 10 / steps)
    return (xListEuler, vxListEuler, eListEuler, time)

# Using the Heun's method to calculate
def getHeunList(steps):
    deltaT = 10 / steps
    vxListHeun = [1]
    xListHeun = [0.5]
    eListHeun = [25/32]
    time = [0]
    for i in range(1, steps):
        xi = xListHeun[i - 1]
        vi = vxListHeun[i - 1]
        x_tilde = xi + vi * deltaT
        v_tilde = vi - 1.5 * 1.5 * xi * deltaT
        xtemp = xi + 1/2 * (vi + v_tilde) * deltaT
        vxtemp = vi - 1/2 * 1.5 * 1.5 * (xi + x_tilde) * deltaT
        xListHeun.append(xtemp)
        vxListHeun.append(vxtemp)
        eListHeun.append(1/2 * (1.5 * 1.5 * xtemp * xtemp + vxtemp * vxtemp))
        time.append(i * 10 / steps)
    return (xListHeun, vxListHeun, eListHeun, time)
