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
ax.set(xlim=[-3, 3],
        ylim=[-2, 2],
        title='Trajectory in Phase Space (Take mass to be 1kg)\nstep $\Delta t= 0.05s$',
        ylabel='Momentum (kg·m/s)',
        xlabel='Position x (m)')
steps_phase = 200
(xListAnalytical_phase, vxListAnalytical_phase, _, _) = getList.getAnalyticalList(steps_phase)
(xListEuler_phase, vxListEuler_phase, _, _) =getList.getEulerList(steps_phase)
(xListHeun_phase, vxListHeun_phase, _, _) =getList.getHeunList(steps_phase)

plot1 = plt.plot(xListAnalytical_phase,
                 vxListAnalytical_phase, # We take the mass of the object to be 1kg to calculate the momentum, following are the same.
                 color='blue',
                 label="Analytical Result")

plot2 = plt.plot(xListEuler_phase, 
                 vxListEuler_phase, 
                 color='red', 
                 label="Euler\'s Method 200 Steps (0.05s)")

plot3 = plt.plot(xListHeun_phase,
                 vxListHeun_phase,
                 color='green',
                 label="Heun\'s Method 200 Steps (0.05s)")

plt.legend(loc='upper right', fontsize="7")

plt.show()
