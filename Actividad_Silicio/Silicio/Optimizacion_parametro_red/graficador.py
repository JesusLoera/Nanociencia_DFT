
import matplotlib.pyplot as plt
import numpy as np
 

a_parameter = np.arange(4.40,4.50,0.01)

energy_ry = [
             -22.83843458,
             -22.83878053,
             -22.83906471,
             -22.83929741,
             -22.83947867,
             -22.83960789,
             -22.83968343,
             -22.83970898,
             -22.83968301,
             -22.83960865
                        ]

energy_ry=np.array(energy_ry)

energy_ev = energy_ry*13.605662285137


fig, axs = plt.subplots(2, 2)

axs[0, 0].scatter(a_parameter, energy_ev)
axs[0, 0].set_title('a VS T. ENERGY (eV)')

axs[0, 1].plot(a_parameter, energy_ev, c='r')
axs[0, 1].scatter(a_parameter, energy_ev)
axs[0, 1].set_title('a VS T. ENERGY (eV)')

axs[1, 0].scatter(a_parameter, energy_ry)
axs[1, 0].set_title('a VS T. ENERGY (Ry)')

axs[1, 1].plot(a_parameter, energy_ry, c='r')
axs[1, 1].scatter(a_parameter, energy_ry)
axs[1, 1].set_title('a VS T. ENERGY (Ry)')

for ax in axs.flat:
    ax.set(xlabel='Lattice Parameter : a (', ylabel='T. ENERGY')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()