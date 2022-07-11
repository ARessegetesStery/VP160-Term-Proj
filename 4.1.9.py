import matplotlib.pyplot as plt
import numpy as np
import math

g,m,alpha,v0=9.8,1,np.pi/8,90
totoltime=10
def getNoDragCoordinates (steps):
    deltaT=totoltime/steps
    xList=[]
    yList=[]
    for j in range (0,steps):
      xList.append(v0*math.cos(alpha)*j*deltaT)
      yList.append(v0*math.sin(alpha)*j*deltaT-0.5*g*(j*deltaT)*(j*deltaT))
    return(xList,yList)

def getQuadraticDragCoordinates(steps):
  deltaT=totoltime/steps
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

def getLinearDragCoordinates(steps):
    vx0 = v0 * math.cos(alpha)
    vy0 = v0 * math.sin(alpha)
    deltaT = totoltime / steps
    vxList = [vx0]
    xList = [0]
    for i in range(1, steps):
        temp = vxList[i - 1] * (1 - k / m * deltaT)
        vxList.append(temp)
        xList.append(xList[i - 1] + vxList[i - 1] * deltaT)
    vyList = [vy0]
    yList = [0]
    for i in range(1, steps):
        temp = vyList[i - 1] * (1 - k / m * deltaT) - g * deltaT
        vyList.append(temp)
        yList.append(yList[i - 1] + vyList[i - 1] * deltaT)
    return(xList,yList)

b=0.05
k=0.7
(xListLinearDrag,yListLinearDrag)=getLinearDragCoordinates(200)
(xListNoDrag,yListNoDrag)=getNoDragCoordinates (200)
(xListQuadraticDrag,yListQuadraticDrag)=getQuadraticDragCoordinates (200)
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax1.set(xlim=[0, 700],
        ylim=[-40, 80],
        title="Trajectories for projectile in different drag conditions",
        ylabel='displacement in y direction (m)',
        xlabel='displacement in x direction (m)')
plot1 = plt.plot(xListLinearDrag,yListLinearDrag, color='red', label='linear drag')
plot2 = plt.plot(xListNoDrag,yListNoDrag, color='orange', label='without drag')
plot3 = plt.plot(xListQuadraticDrag,yListQuadraticDrag, color='blue', label='quadratic drag')
plt.legend(loc='upper right', fontsize="8")
plt.show()