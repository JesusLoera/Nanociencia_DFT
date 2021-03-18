
import matplotlib.pyplot as plt
import numpy as np


ecutwfc=[]
ecutwfc= np.array(ecutwfc)

for i in range (20, 55, 5):

    ecutwfc = np.append(ecutwfc,i)

ecutrho = ecutwfc*8

print(ecutrho)
print(len(ecutrho))

energy_ry = [
            -22.83619488,
            -22.83752692,
            -22.83801485,
            -22.83809604,
            -22.83814263,
            -22.83819739,
            -22.83823768
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