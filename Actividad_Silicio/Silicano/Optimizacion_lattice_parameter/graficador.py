
import matplotlib.pyplot as plt
import numpy as np
 

a_parameter = np.arange(3.0,5.1,0.1)

energy_ry = [
             -24.24486449,
             -24.49683231,
             -24.69422901,
             -24.84625804,
             -24.960538  ,
             -25.04365867,
             -25.10107835,
             -25.13740916,
             -25.15645118,
             -25.16152118,
             -25.15535363,
             -25.14025934,
             -25.11820221,
             -25.09086041,
             -25.0596043 ,
             -25.02559224,
             -24.98980588,
             -24.95316997,
             -24.91651276,
             -24.8799504 ,
             -24.84379828
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