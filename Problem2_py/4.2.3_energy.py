import Functions4_2 as getList
import matplotlib.pyplot as plt

fig = plt.figure()

plt.subplots_adjust(left=None,
                    bottom=None,
                    right=None,
                    top=None,
                    wspace=0.6,
                    hspace=0.8)

# start drawing the energy graph E(t)
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[0, 10],
        ylim=[-3, 3],
        title='Graph E(t)\nstep $\Delta t= 0.05s, 0.01s, 0.005s$',
        ylabel='Energy (J)',
        xlabel='Time t (s)')
steps1 = 200
(_, _, eListAnalytical, time0) = getList.getAnalyticalList(steps1)
(_, _, eListEuler_1, time1) =getList.getEulerList(steps1)
steps2 = 1000
(_, _, eListEuler_2, time2) =getList.getEulerList(steps2)
steps3 = 2000
(_, _, eListEuler_3, time3) =getList.getEulerList(steps3)

plot1 = plt.plot(time0,
                 eListAnalytical,
                 color='blue',
                 label="Analytical Result")

plot2 = plt.plot(time1, 
                 eListEuler_1, 
                 color='red', 
                 label="Euler\'s Method 200 Steps (0.05s)")

plot3 = plt.plot(time2,
                 eListEuler_2,
                 color='green',
                 label="Euler\'s Method 1000 Steps (0.01s)")

plot4 = plt.plot(time3,
                 eListEuler_3,
                 color='orange',
                 label="Euler\'s Method 2000 Steps (0.005s)")

plt.legend(loc='upper right', fontsize="7")

plt.show()
