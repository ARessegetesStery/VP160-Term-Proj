import matplotlib.pyplot as plt
import numpy as np
import math


def getxList(steps):
    vx0 = v0 * math.cos(alpha)
    deltaT = 8 / steps
    vxListEuler = [vx0]
    xListEuler = [0]
    for i in range(1, steps):
        temp = vxListEuler[i - 1] * (1 - k / m * deltaT)
        vxListEuler.append(temp)
        xListEuler.append(xListEuler[i - 1] + vxListEuler[i - 1] * deltaT)

    xListAnalytical = []
    for j in range(0, steps):
        xListAnalytical.append(vx0 * m / k *
                              (1 - math.exp(-k / m * deltaT * j)))
    return (xListEuler, xListAnalytical)


def getyList(steps):
    t = np.linspace(start=0, stop=8, num=steps)
    vy0 = v0 * math.sin(alpha)
    deltaT = 8 / steps
    g = 9.8
    vyListEuler = [vy0]
    yListEuler = [0]
    for i in range(1, steps):
        temp = vyListEuler[i - 1] * (1 - k / m * deltaT) - g * deltaT
        vyListEuler.append(temp)
        yListEuler.append(yListEuler[i - 1] + vyListEuler[i - 1] * deltaT)

    yListAnalytical = []
    for j in range(0, steps):
        yListAnalytical.append((vy0 + m * g / k) * m / k *
                              (1 - math.exp(-k / m * j * deltaT)) -
                              m * g / k * j * deltaT)
    return (yListEuler, yListAnalytical)


fig = plt.figure()

alpha, m, k, v0 = np.pi/6, 1, 1, 90  # the variables

plt.subplots_adjust(left=None,
                    bottom=None,
                    right=None,
                    top=None,
                    wspace=0.6,
                    hspace=0.8)
# start drawing the first picture
ax1 = fig.add_subplot(2, 2, 1)
ax1.set(xlim=[0, 100],
        ylim=[0, 50],
        title=r'step $\Delta t=0.08s$',
        ylabel='displacement in y direction (m)',
        xlabel='displacement in x direction (m)')
steps1 = 100
(xListEuler1, xListAnalytical1) = getxList(steps1)
(yListEuler1, yListAnalytical1) = getyList(steps1)
plot1 = plt.plot(xListEuler1, yListEuler1, color='red', label="Euler\' Method")
plot2 = plt.plot(xListAnalytical1,
                 yListAnalytical1,
                 color='blue',
                 label="Analytical")
plt.legend(loc='upper right', fontsize="7")

# start drawing the second picture
ax2 = fig.add_subplot(2, 2, 2)
ax2.set(xlim=[0, 100],
        ylim=[0, 50],
        title=r'step $\Delta t=0.107s$',
        ylabel='displacement in y direction (m)',
        xlabel='displacement in x direction (m)')
steps2 = 75
(xListEuler2, xListAnalytical2) = getxList(steps2)
(yListEuler2, yListAnalytical2) = getyList(steps2)
plot3 = plt.plot(xListEuler2, yListEuler2, color='red', label="Euler\' Method")
plot4 = plt.plot(xListAnalytical2,
                 yListAnalytical2,
                 color='blue',
                 label="Analytical")
plt.legend(loc='upper right', fontsize="7")

# start drawing the third picture
ax3 = fig.add_subplot(2, 2, 3)
ax3.set(xlim=[0, 100],
        ylim=[0, 50],
        title=r'step $\Delta t=0.16s$',
        ylabel='displacement in y direction (m)',
        xlabel='displacement in x direction (m)')
steps3 = 50
(xListEuler3, xListAnalytical3) = getxList(steps3)
(yListEuler3, yListAnalytical3) = getyList(steps3)
plot5 = plt.plot(xListEuler3, yListEuler3, color='red', label="Euler\' Method")
plot6 = plt.plot(xListAnalytical3,
                 yListAnalytical3,
                 color='blue',
                 label="Analytical")
plt.legend(loc='upper right', fontsize="7")

# start drawing the fourth picture (check sensitivity)
ax3 = fig.add_subplot(2, 2, 4)
ax3.set(xlim=[0, 100],
        ylim=[0, 50],
        title='Sensitivity Examination',
        ylabel='displacement in y direction (m)',
        xlabel='displacement in x direction (m)')
steps1=100
steps2=75
steps3 =50
# get x
(xListEuler1, xListAnalytical1) = getxList(steps1)
(xListEuler2, xListAnalytical2) = getxList(steps2)
(xListEuler3, xListAnalytical3) = getxList(steps3)
# get y
(yListEuler1, yListAnalytical1) = getyList(steps1)
(yListEuler2, yListAnalytical2) = getyList(steps2)
(yListEuler3, yListAnalytical3) = getyList(steps3)
plot7 = plt.plot(xListEuler1, yListEuler1, color='red', label=r"$step\quad \Delta t=0.08s$")
plot8 = plt.plot(xListEuler2, yListEuler2,color='blue',label=r"$step\quad \Delta t=0.107s$")
plot9 = plt.plot(xListEuler3, yListEuler3,color='orange',label=r"$step\quad \Delta t=0.16s$")
plt.legend(loc='upper right', fontsize="7")
plt.show()
