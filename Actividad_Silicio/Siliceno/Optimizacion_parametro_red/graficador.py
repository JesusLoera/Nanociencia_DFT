
import matplotlib.pyplot as plt
import numpy as np
 

a_parameter = np.arange(3.0,4.6,0.1)

energy_ry = [
             -22.13376217,
             -22.30409205,
             -22.43782533,
             -22.54158996,
             -22.6187458,
             -22.67399165,
             -22.71117223,
             -22.73359655,
             -22.74409828,
             -22.74509223,
             -22.73864451,
             -22.72650259,
             -22.71017072,
             -22.69107727,
             -22.67091028,
             -22.64936146 
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