import matplotlib.pyplot as plt
import numpy as np
import math

m,k,v0=1,1,90
steps=500
alpha=np.pi/6
g=9.8
def getEulerCoordinates(b):
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
ax1.set(xlim=[0, 90],
        ylim=[0, 40],
        title=r'$Numerical\quad Method\quad with\quad step\quad \Delta t=0.016s$',
        ylabel='displacement in y direction (m)',
        xlabel='displacement in x direction (m)')
(XEulerList1, yEulerList1) = getEulerCoordinates(0.03)
(XEulerList2, yEulerList2) = getEulerCoordinates(0.05)
(XEulerList3, yEulerList3) = getEulerCoordinates(0.07)
(XEulerList4, yEulerList4) = getEulerCoordinates(0.09)
(XEulerList5, yEulerList5) = getEulerCoordinates(0.11)
plot1 = plt.plot(XEulerList1, yEulerList1, color='red', label='b=0.03')
plot2 = plt.plot(XEulerList2, yEulerList2, color='orange', label='b=0.05')
plot3 = plt.plot(XEulerList3, yEulerList3, color='blue', label='b=0.07')
plot3 = plt.plot(XEulerList4, yEulerList4, color='green', label='b=0.09')
plot3 = plt.plot(XEulerList5, yEulerList5, color='purple', label='b=0.11')
plt.legend(loc='upper right', fontsize="12")
plt.show()