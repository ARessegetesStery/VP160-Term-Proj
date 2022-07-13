import Functions4_2 as getList
import matplotlib.pyplot as plt

fig = plt.figure()

plt.subplots_adjust(left=None,
                    bottom=None,
                    right=None,
                    top=None,
                    wspace=0.6,
                    hspace=0.8)

# start drawing the Trajectory in Phase Space (with Heun's method)
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[0, 10],
        ylim=[-3, 3],
        title='Graph E(t)\nstep $\Delta t= 0.05s$',
        ylabel='Energy (J)',
        xlabel='Time t (s)')
steps = 200
(_, _, eListAnalytical, time_phase) = getList.getAnalyticalList(steps)
(_, _, eListEuler, _) =getList.getEulerList(steps)
(_, _, eListHeun, _) =getList.getHeunList(steps)

plot1 = plt.plot(time_phase,
                 eListAnalytical,
                 color='blue',
                 label="Analytical Result")

plot2 = plt.plot(time_phase, 
                 eListEuler, 
                 color='red', 
                 label="Euler\'s Method 200 Steps (0.05s)")

plot3 = plt.plot(time_phase,
                 eListHeun,
                 color='green',
                 label="Heun\'s Method 200 Steps (0.05s)")

plt.legend(loc='upper right', fontsize="7")

plt.show()
