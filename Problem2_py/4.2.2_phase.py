import Functions4_2 as getList
import matplotlib.pyplot as plt

fig = plt.figure()

plt.subplots_adjust(left=None,
                    bottom=None,
                    right=None,
                    top=None,
                    wspace=0.6,
                    hspace=0.8)

# start drawing the Trajectory in Phase Space
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[-3, 3],
        ylim=[-2, 2],
        title='Trajectory in Phase Space (Take mass to be 1kg)\nstep $\Delta t= 0.05s, 0.01s, 0.005s$',
        ylabel='Momentum (kg·m/s)',
        xlabel='Position x (m)')
steps_phase_1 = 200
(xListAnalytical_phase, vxListAnalytical_phase, _, _) = getList.getAnalyticalList(steps_phase_1)
(xListEuler_phase_1, vxListEuler_phase_1, _, _) =getList.getEulerList(steps_phase_1)
steps_phase_2 = 1000
(xListEuler_phase_2, vxListEuler_phase_2, _, _) =getList.getEulerList(steps_phase_2)
steps_phase_3 = 2000
(xListEuler_phase_3, vxListEuler_phase_3, _, _) =getList.getEulerList(steps_phase_3)

plot1 = plt.plot(xListAnalytical_phase,
                 vxListAnalytical_phase, # We take the mass of the object to be 1kg to calculate the momentum, following are the same.
                 color='blue',
                 label="Analytical Result")

plot2 = plt.plot(xListEuler_phase_1, 
                 vxListEuler_phase_1, 
                 color='red', 
                 label="Euler\'s Method 200 Steps (0.05s)")

plot3 = plt.plot(xListEuler_phase_2,
                 vxListEuler_phase_2,
                 color='green',
                 label="Euler\'s Method 1000 Steps (0.01s)")

plot4 = plt.plot(xListEuler_phase_3,
                 vxListEuler_phase_3,
                 color='orange',
                 label="Euler\'s Method 2000 Steps (0.005s)")

plt.legend(loc='upper right', fontsize="7")

plt.show()
