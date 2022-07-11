import matplotlib.pyplot as plt
import numpy as np
import math

b,m,k,v0=0.05,1,1,90
steps=500
g=9.8
def getEulerCoordinates(alpha):
  deltaT=8/steps
  v0x=v0*math.cos(alpha)
  v0y=v0*math.sin(alpha)
  vxList=[v0x]
  vyList=[v0y]
  xList=[0]
  yList=[0]
  for i in range(0,steps):
    vxList.append(vxList[i]*(1-b/m*math.sqrt(vxList[i]*vxList[i]+vyList[i]*vyList[i])*deltaT))
    vyList.append(-g*deltaT+vyList[i]*(1-b/m*math.sqrt(vxList[i]*vxList[i]+vyList[i]*vyList[i])*deltaT))
  for j in range(1,steps):
    xList.append(xList[j-1]+vxList[j-1]*deltaT)
    yList.append(yList[j-1]+vyList[j-1]*deltaT)
  return(xList,yList)

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax1.set(xlim=[0, 60],
        ylim=[0, 40],
        title=r'$Numerical\quad Method\quad with\quad step\quad \Delta t=0.016s$',
        ylabel='displacement in y direction (m)',
        xlabel='displacement in x direction (m)')
(XEulerList1, yEulerList1) = getEulerCoordinates(np.pi/3)
(XEulerList2, yEulerList2) = getEulerCoordinates(np.pi/4)
(XEulerList3, yEulerList3) = getEulerCoordinates(np.pi/5)
(XEulerList4, yEulerList4) = getEulerCoordinates(np.pi/6)
(XEulerList5, yEulerList5) = getEulerCoordinates(np.pi/7)
plot1 = plt.plot(XEulerList1, yEulerList1, color='red', label=r'$\alpha=\frac{\pi}{3}$')
plot2 = plt.plot(XEulerList2, yEulerList2, color='orange', label=r'$\alpha=\frac{\pi}{4}$')
plot3 = plt.plot(XEulerList3, yEulerList3, color='blue', label=r'$\alpha=\frac{\pi}{5}$')
plot3 = plt.plot(XEulerList4, yEulerList4, color='green', label=r'$\alpha=\frac{\pi}{6}$')
plot3 = plt.plot(XEulerList5, yEulerList5, color='purple', label=r'$\alpha=\frac{\pi}{7}$')
plt.legend(loc='upper right', fontsize="12")
plt.show()