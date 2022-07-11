import matplotlib.pyplot as plt
import numpy as np
import math

b,m,k,v0=0.05,1,1,90
steps=500
g=9.8
def getEulerSpeed(alpha):
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
EulerList1 = getEulerSpeed(np.pi/3)
EulerList2 = getEulerSpeed(np.pi/4)
EulerList3 = getEulerSpeed(np.pi/5)
EulerList4 = getEulerSpeed(np.pi/6)
EulerList5 = getEulerSpeed(np.pi/7)
plot1 = plt.plot(t,EulerList1, color='red', label=r'$\alpha=\frac{\pi}{3}$')
plot2 = plt.plot(t,EulerList2,color='orange', label=r'$\alpha=\frac{\pi}{4}$')
plot3 = plt.plot(t,EulerList3, color='blue', label=r'$\alpha=\frac{\pi}{5}$')
plot3 = plt.plot(t,EulerList4, color='green', label=r'$\alpha=\frac{\pi}{6}$')
plot3 = plt.plot(t,EulerList5,  color='purple', label=r'$\alpha=\frac{\pi}{7}$')
plt.legend(loc='upper right', fontsize="7")
plt.show()