import matplotlib.pyplot as plt
import numpy as np
import math
steps,m, k, v0 = 100,1, 1, 90  # the variables
alpha=np.pi/6
def getCoordinateList():
    vx0 = v0 * math.cos(alpha)
    vy0 = v0 * math.sin(alpha)
    deltaT = 0.08
    g = 9.8
    t = np.linspace(start=0, stop=8, num=steps)
    vxListNumerical = []
    vyListNumerical = []
    for j in range(0, steps):
        vxListNumerical.append(vx0*math.exp(-k/m*j*deltaT))
    for j in range(0, steps):
        vyListNumerical.append((vy0+m*g/k)*math.exp(-k/m*j*deltaT)-m*g/k)
    speed=[]
    for j in range(0,steps):
        speed.append(math.sqrt(vxListNumerical[j]**2+vyListNumerical[j]**2))
    return (speed,t)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[0, 8],
        ylim=[0, 100],
        title=r'step $\Delta t=0.08s$',
        ylabel='speed of the particle (m/s)',
        xlabel='time (s)')
(speed,t)=getCoordinateList()
plot1 = plt.plot(t,speed, color='red', label='speed')
plt.legend(loc='upper right', fontsize="7")
plt.show()