import matplotlib.pyplot as plt
import numpy as np
import math
steps,m, k, v0 = 100,1, 1, 90  # the variables
def getCoordinateList(alpha):
  
    vx0 = v0 * math.cos(alpha)
    vy0 = v0 * math.sin(alpha)
    deltaT = 0.08
    g = 9.8
    xListAnalytical = []
    yListAnalytical = []
    for j in range(0, steps):
        xListAnalytical.append(vx0 * m / k *
                              (1 - math.exp(-k / m * deltaT * j)))
    for j in range(0, steps):
        yListAnalytical.append((vy0 + m * g / k) * m / k *
                              (1 - math.exp(-k / m * j * deltaT)) -
                              m * g / k * j * deltaT)
    return (xListAnalytical,yListAnalytical)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[0, 100],
        ylim=[0, 50],
        title=r'step $\Delta t=0.08s$',
        ylabel='displacement in y direction (m)',
        xlabel='displacement in x direction (m)')
steps1 = 100
(xListAnalytical1,yListAnalytical1) = getCoordinateList(np.pi/4)
(xListAnalytical2,yListAnalytical2) = getCoordinateList(np.pi/5)
(xListAnalytical3,yListAnalytical3) = getCoordinateList(np.pi/6)
(xListAnalytical4,yListAnalytical4) = getCoordinateList(np.pi/7)
(xListAnalytical5,yListAnalytical5) = getCoordinateList(np.pi/8)
plot1 = plt.plot(xListAnalytical1,yListAnalytical1, color='red', label=r'$\alpha=\pi/4$')
plot2 = plt.plot(xListAnalytical2,yListAnalytical2, color='blue', label=r'$\alpha=\pi/5$')
plot3 = plt.plot(xListAnalytical3,yListAnalytical3, color='green', label=r'$\alpha=\pi/6$')
plot4 = plt.plot(xListAnalytical4,yListAnalytical4, color='orange', label=r'$\alpha=\pi/7$') 
plot5 = plt.plot(xListAnalytical5,yListAnalytical5, color='purple', label=r'$\alpha=\pi/8$') 
plt.legend(loc='upper right', fontsize="7")
plt.show()