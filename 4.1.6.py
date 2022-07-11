import matplotlib.pyplot as plt
import numpy as np
import math

b,m,k,v0=0.05,1,1,90
alpha=np.pi/6
g=9.8
def getEulerCoordinates(steps):
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
        ylim=[0, 20],
        title=r'Sensitivity Examination',
        ylabel='displacement in y direction (m)',
        xlabel='displacement in x direction (m)')
(XEulerList1, yEulerList1) = getEulerCoordinates(100)
(XEulerList2, yEulerList2) = getEulerCoordinates(50)
(XEulerList3, yEulerList3) = getEulerCoordinates(500)
plot1 = plt.plot(XEulerList1, yEulerList1, color='red', label=r'$step\quad \Delta t=0.08s$')
plot2 = plt.plot(XEulerList2, yEulerList2, color='orange', label=r'$step\quad \Delta t=0.16s$')
plot3 = plt.plot(XEulerList3, yEulerList3, color='blue', label=r'$step\quad \Delta t=0.016s$')
plt.legend(loc='upper right', fontsize="7")
plt.show()