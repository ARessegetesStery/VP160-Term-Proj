import matplotlib.pyplot as plt
import numpy as np
import math

m,k,v0=1,1,90
steps=500
alpha=np.pi/6
g=9.8
def getEulerSpeed(b):
  deltaT=8/steps
  v0x=v0*math.cos(alpha)
  v0y=v0*math.sin(alpha)
  vxList=[v0x]
  vyList=[v0y]
  for i in range(0,steps):
    vxList.append(vxList[i]*(1-b/m*math.sqrt(vxList[i]*vxList[i]+vyList[i]*vyList[i])*deltaT))
    vyList.append(-g*deltaT+vyList[i]*(1-b/m*math.sqrt(vxList[i]*vxList[i]+vyList[i]*vyList[i])*deltaT))
  vList=[v0]
  for i in range(1,steps):
    vList.append(math.sqrt(vxList[i]*vxList[i]+vyList[i]*vyList[i]))
  return vList


fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax1.set(xlim=[0, 8],
        ylim=[0, 40],
        title=r'$Numerical\quad Method\quad with\quad step\quad \Delta t=0.016s$',
        ylabel='speed of the particle (m/s)',
        xlabel='time (s)')
t=np.linspace(0,8,500)
EulerList1 = getEulerSpeed(0.03)
EulerList2 = getEulerSpeed(0.05)
EulerList3 = getEulerSpeed(0.07)
EulerList4 = getEulerSpeed(0.09)
EulerList5 = getEulerSpeed(0.11)
plot1 = plt.plot(t,EulerList1, color='red', label='b=0.03')
plot2 = plt.plot(t,EulerList2,color='orange', label='b=0.05')
plot3 = plt.plot(t,EulerList3, color='blue', label='b=0.07')
plot3 = plt.plot(t,EulerList4, color='green', label='b=0.09')
plot3 = plt.plot(t,EulerList5,  color='purple', label='b=0.11')
plt.legend(loc='upper right', fontsize="7")
plt.show()