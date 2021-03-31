
import matplotlib.pyplot as plt
import numpy as np


labels = np.arange(4,21)

energy_ry = [
             -25.15462425,
             -25.1592368 ,
             -25.16080697,
             -25.1613319 ,
             -25.16155611,
             -25.16166872,
             -25.16168509,
             -25.16170196,
             -25.16171919,
             -25.16171234,
             -25.16171343,
             -25.16172526,
             -25.16171521,
             -25.1617141 ,
             -25.16172664,
             -25.16171548,
             -25.16171448
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
    ax.set(xlabel='i in K_POINTS: i i 1 0 0 0', ylabel='T. ENERGY')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()