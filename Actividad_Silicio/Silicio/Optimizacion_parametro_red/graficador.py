
import matplotlib.pyplot as plt
import numpy as np
 

a_parameter = np.arange(4.4,6.5,0.1)

energy_ry = [
             -22.28953734,
             -22.41445715,
             -22.51757106,
             -22.60213758,
             -22.67043750,
             -22.72445699,
             -22.76596421,
             -22.79670908,
             -22.81816880,
             -22.83167548,
             -22.83843458,
             -22.83948630,
             -22.83578673,
             -22.82814903,
             -22.81730795,
             -22.80390089,
             -22.78848485,
             -22.77158355,
             -22.75362525,
             -22.73486812,
             -22.71559502
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