import Functions4_2 as getList
import matplotlib.pyplot as plt

fig = plt.figure()

plt.subplots_adjust(left=None,
                    bottom=None,
                    right=None,
                    top=None,
                    wspace=0.6,
                    hspace=0.8)

# start drawing the Trajectory in Configuration Space (with Heun's method)
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[0, 10],
        ylim=[-2, 2],
        title='Trajectory in Configuration Space\nstep $\Delta t= 0.05s$',
        ylabel='Displacement x (m)',
        xlabel='Time t (s)')
steps_configuration = 200
(xListAnalytical_configuration, _, _, time_configuration) = getList.getAnalyticalList(steps_configuration)
(xListEuler_configuration, _, _, _) =getList.getEulerList(steps_configuration)
(xListHeun_configuration, _, _, _) =getList.getHeunList(steps_configuration)

plot1 = plt.plot(time_configuration,
                 xListAnalytical_configuration,
                 color='blue',
                 label="Analytical Result")

plot2 = plt.plot(time_configuration, 
                 xListEuler_configuration, 
                 color='red', 
                 label="Euler\'s Method 200 Steps (0.05s)")

plot3 = plt.plot(time_configuration,
                 xListHeun_configuration,
                 color='green',
                 label="Heun\'s Method 200 Steps (0.05s)")

plt.legend(loc='upper right', fontsize="7")

plt.show()
