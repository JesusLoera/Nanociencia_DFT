
import matplotlib.pyplot as plt
import numpy as np


ecutwfc=[]
ecutwfc= np.array(ecutwfc)

for i in range (20, 55, 5):

    ecutwfc = np.append(ecutwfc,i)

energy_ry = [
            -25.14328702,
            -25.15410831,
            -25.15932189,
            -25.16173177,
            -25.1628564,
            -25.16340404,
            -25.16365325
                        ]

energy_ry=np.array(energy_ry)

energy_ev = energy_ry*13.605662285137


fig, axs = plt.subplots(2, 2)

axs[0, 0].scatter(ecutwfc, energy_ev)
axs[0, 0].set_title('ECUTWFC VS T. ENERGY (eV)')

axs[0, 1].plot(ecutwfc, energy_ev, c='r')
axs[0, 1].scatter(ecutwfc, energy_ev)
axs[0, 1].set_title('ECUTWFC VS T. ENERGY (eV)')

axs[1, 0].scatter(ecutwfc, energy_ry)
axs[1, 0].set_title('ECUTWFC VS T. ENERGY (Ry)')

axs[1, 1].plot(ecutwfc, energy_ry, c='r')
axs[1, 1].scatter(ecutwfc, energy_ry)
axs[1, 1].set_title('ECUTWFC VS T. ENERGY (Ry)')

for ax in axs.flat:
    ax.set(xlabel='ECUTWFC', ylabel='T. ENERGY')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()