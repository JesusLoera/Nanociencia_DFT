
import matplotlib.pyplot as plt
import numpy as np


labels = np.arange(6,13)

energy_ry = [
            -22.83690926,
            -22.83801485,
            -22.83843458,
            -22.83860108,
            -22.83867074,
            -22.83869764,
            -22.83871111
                        ]

energy_ry=np.array(energy_ry)

energy_ev = energy_ry*13.605662285137


fig, axs = plt.subplots(2, 2)

axs[0, 0].scatter(labels, energy_ev)
axs[0, 0].set_title('i VS T. ENERGY (eV)')

axs[0, 1].plot(labels, energy_ev, c='r')
axs[0, 1].scatter(labels, energy_ev)
axs[0, 1].set_title('i VS T. ENERGY (eV)')

axs[1, 0].scatter(labels, energy_ry)
axs[1, 0].set_title('i VS T. ENERGY (Ry)')

axs[1, 1].plot(labels, energy_ry, c='r')
axs[1, 1].scatter(labels, energy_ry)
axs[1, 1].set_title('i VS T. ENERGY (Ry)')

for ax in axs.flat:
    ax.set(xlabel='i in K_POINTS: i i i 0 0 0', ylabel='T. ENERGY')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()