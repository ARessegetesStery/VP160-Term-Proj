import Functions4_2 as getList
import matplotlib.pyplot as plt

fig = plt.figure()

plt.subplots_adjust(left=None,
                    bottom=None,
                    right=None,
                    top=None,
                    wspace=0.6,
                    hspace=0.8)

# start drawing the Trajectory in Configuration Space
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[0, 10],
        ylim=[-2, 2],
        title='Trajectory in Configuration Space\nstep $\Delta t= 0.05s, 0.01s, 0.005s$',
        ylabel='Displacement x (m)',
        xlabel='Time t (s)')
steps_configuration_1 = 200
(xListAnalytical_configuration, _, _, time_configuration_0) = getList.getAnalyticalList(steps_configuration_1)
(xListEuler_configuration_1, _, _, time_configuration_1) =getList.getEulerList(steps_configuration_1)
steps_configuration_2 = 1000
(xListEuler_configuration_2, _, _, time_configuration_2) =getList.getEulerList(steps_configuration_2)
steps_configuration_3 = 2000
(xListEuler_configuration_3, _, _, time_configuration_3) =getList.getEulerList(steps_configuration_3)

plot1 = plt.plot(time_configuration_0,
                 xListAnalytical_configuration,
                 color='blue',
                 label="Analytical Result")

plot2 = plt.plot(time_configuration_1, 
                 xListEuler_configuration_1, 
                 color='red', 
                 label="Euler\'s Method 200 Steps (0.05s)")

plot3 = plt.plot(time_configuration_2,
                 xListEuler_configuration_2,
                 color='green',
                 label="Euler\'s Method 1000 Steps (0.01s)")

plot4 = plt.plot(time_configuration_3,
                 xListEuler_configuration_3,
                 color='orange',
                 label="Euler\'s Method 2000 Steps (0.005s)")

plt.legend(loc='upper right', fontsize="7")

plt.show()
