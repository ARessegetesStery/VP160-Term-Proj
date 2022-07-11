import matplotlib.pyplot as plt
import numpy as np
import math
steps,m, k, v0 = 100,1, 1, 90  # the variables
def getCoordinateList(alpha):
    vx0 = v0 * math.cos(alpha)
    vy0 = v0 * math.sin(alpha)
    deltaT = 0.08
    g = 9.8
    t = np.linspace(start=0, stop=8, num=steps)
    vxListAnalytical = []
    vyListAnalytical = []
    for j in range(0, steps):
        vxListAnalytical.append(vx0*math.exp(-k/m*j*deltaT))
    for j in range(0, steps):
        vyListAnalytical.append((vy0+m*g/k)*math.exp(-k/m*j*deltaT)-m*g/k)
    speed=[]
    for j in range(0,steps):
        speed.append(math.sqrt(vxListAnalytical[j]**2+vyListAnalytical[j]**2))
    return (speed,t)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[0, 8],
        ylim=[0, 100],
        title=r'step $\Delta t=0.08s$',
        ylabel='speed of the particle (m/s)',
        xlabel='time (s)')
(speed1,t1)=getCoordinateList(np.pi/4)
(speed2,t2)=getCoordinateList(np.pi/5)
(speed3,t3)=getCoordinateList(np.pi/6)
(speed4,t4)=getCoordinateList(np.pi/7)
(speed5,t5)=getCoordinateList(np.pi/8)
plot1 = plt.plot(t1,speed1, color='red', label=r'$\alpha=\pi/4$')
plot2 = plt.plot(t2,speed2, color='blue', label=r'$\alpha=\pi/5$')
plot3 = plt.plot(t3,speed3, color='green', label=r'$\alpha=\pi/6$')
plot4 = plt.plot(t4,speed4, color='orange', label=r'$\alpha=\pi/7$') 
plot5 = plt.plot(t5,speed5, color='purple', label=r'$\alpha=\pi/8$') 
plt.legend(loc='upper right', fontsize="7")
plt.show()