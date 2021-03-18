
import matplotlib.pyplot as plt
import numpy as np


ecutwfc = 30

k_ecutrho = np.arange(3,13)


for i in range (20, 55, 5):

    ecutwfc = np.append(ecutwfc,i)

ecutwfc = ecutwfc*30

print(k_ecutrho)
print(len(k_ecutrho))

energy_ry = [
            -22.83804028,
            -22.83801202,
            -22.83804410,
            -22.83801447,
            -22.83801788,
            -22.83801485,
            -22.83801427,
            -22.83801875,
            -22.83801848,
            -22.83801992
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