
import matplotlib.pyplot as plt
import numpy as np
 

a_parameter = np.arange(3.80,3.9,0.01)

energy_ry = [
             -22.74409492,
             -22.74458629,
             -22.74498419,
             -22.74529346,
             -22.74551349,
             -22.7456486 ,
             -22.74569668,
             -22.74565931,
             -22.7455456 ,
             -22.74535466,
             -22.74508828
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