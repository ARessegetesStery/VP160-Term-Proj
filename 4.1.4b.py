import matplotlib.pyplot as plt
import numpy as np
import math
steps,m, v0 = 100,1, 90  # the variables
alpha=np.pi/6
g=9.8
def getCoordinateList(k):
    t=np.linspace(0,8,steps)
    vx0 = v0 * math.cos(alpha)
    vy0 = v0 * math.sin(alpha)
    deltaT = 8 / steps
    vxListEuler = [vx0]
    for i in range(1, steps):
        temp = vxListEuler[i - 1] * (1 - k / m * deltaT)
        vxListEuler.append(temp)
    vyListEuler = [vy0]
    for i in range(1, steps):
        temp = vyListEuler[i - 1] * (1 - k / m * deltaT) - g * deltaT
        vyListEuler.append(temp)
    speed=[]
    for j in range(0,steps):
        speed.append(math.sqrt(vxListEuler[j]**2+vyListEuler[j]**2))
    return (speed,t)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[0, 8],
        ylim=[0, 100],
        title=r'step $\Delta t=0.08s$',
        ylabel='speed of the particle (m/s)',
        xlabel='time (s)')
(speed1,t1)=getCoordinateList(0.5)
(speed2,t2)=getCoordinateList(0.75)
(speed3,t3)=getCoordinateList(1)
(speed4,t4)=getCoordinateList(1.25)
(speed5,t5)=getCoordinateList(1.5)
plot1 = plt.plot(t1,speed1, color='red', label='k=0.5')
plot2 = plt.plot(t2,speed2, color='blue', label='k=0.75')
plot3 = plt.plot(t3,speed3, color='green', label='k=1')
plot4 = plt.plot(t4,speed4, color='orange', label='k=1.25') 
plot5 = plt.plot(t5,speed5, color='purple', label='k=1.5') 
plt.legend(loc='upper right', fontsize="7")
plt.show()