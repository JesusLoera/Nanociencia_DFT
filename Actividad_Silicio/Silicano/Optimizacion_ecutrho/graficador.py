
import matplotlib.pyplot as plt
import numpy as np

k_ecutrho = np.arange(4,13)


energy_ry = [
             -25.16187741,
             -25.16175392,
             -25.16172591,
             -25.16172131,
             -25.16173177,
             -25.1617316,
             -25.16172779,
             -25.16173063,
             -25.16172966
                        ]

energy_ry=np.array(energy_ry)

energy_ev = energy_ry*13.605662285137


fig, axs = plt.subplots(2, 2)

axs[0, 0].scatter(k_ecutrho, energy_ev)
axs[0, 0].set_title('K VS T. ENERGY (eV)')

axs[0, 1].plot(k_ecutrho, energy_ev, c='r')
axs[0, 1].scatter(k_ecutrho, energy_ev)
axs[0, 1].set_title('K VS T. ENERGY (eV)')

axs[1, 0].scatter(k_ecutrho, energy_ry)
axs[1, 0].set_title('K VS T. ENERGY (Ry)')

axs[1, 1].plot(k_ecutrho, energy_ry, c='r')
axs[1, 1].scatter(k_ecutrho, energy_ry)
axs[1, 1].set_title('K VS T. ENERGY (Ry)')

for ax in axs.flat:
    ax.set(xlabel='K in ecutrho = k*ecutwfc', ylabel='T. ENERGY')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()