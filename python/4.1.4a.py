import matplotlib.pyplot as plt
import numpy as np
import math
alpha,steps,m,v0 = np.pi/6,100,1, 90  # the variables
g=9.8
def getCoordinateList(k):
    vx0 = v0 * math.cos(alpha)
    vy0 = v0 * math.sin(alpha)
    deltaT = 8 / steps
    vxListEuler = [vx0]
    xListEuler = [0]
    for i in range(1, steps):
        temp = vxListEuler[i - 1] * (1 - k / m * deltaT)
        vxListEuler.append(temp)
        xListEuler.append(xListEuler[i - 1] + vxListEuler[i - 1] * deltaT)
    vyListEuler = [vy0]
    yListEuler = [0]
    for i in range(1, steps):
        temp = vyListEuler[i - 1] * (1 - k / m * deltaT) - g * deltaT
        vyListEuler.append(temp)
        yListEuler.append(yListEuler[i - 1] + vyListEuler[i - 1] * deltaT)
    return(xListEuler,yListEuler)



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[0, 175],
        ylim=[0, 50],
        title=r'step $\Delta t=0.08s$',
        ylabel='displacement in y direction (m)',
        xlabel='displacement in x direction (m)')
steps1 = 100
(xListAnalytical1,yListAnalytical1) = getCoordinateList(0.5)
(xListAnalytical2,yListAnalytical2) = getCoordinateList(0.75)
(xListAnalytical3,yListAnalytical3) = getCoordinateList(1)
(xListAnalytical4,yListAnalytical4) = getCoordinateList(1.25)
(xListAnalytical5,yListAnalytical5) = getCoordinateList(1.5)
plot1 = plt.plot(xListAnalytical1,yListAnalytical1, color='red', label='k=0.5')
plot2 = plt.plot(xListAnalytical2,yListAnalytical2, color='blue', label='k=0.75')
plot3 = plt.plot(xListAnalytical3,yListAnalytical3, color='green', label='k=1')
plot4 = plt.plot(xListAnalytical4,yListAnalytical4, color='orange', label='k=1.25') 
plot5 = plt.plot(xListAnalytical5,yListAnalytical5, color='purple', label='k=1.5') 
plt.legend(loc='upper right', fontsize="14")
plt.show()