import numpy as np
import matplotlib.pyplot as plt

Atom_1_1s = 'test.pdos_atm#1(Si)_wfc#1(s)'
Atom_1_2p = 'test.pdos_atm#1(Si)_wfc#2(p)'
Atom_2_1s = 'test.pdos_atm#2(Si)_wfc#1(s)'
Atom_2_2p = 'test.pdos_atm#2(Si)_wfc#2(p)'

energy_eV_data = np.loadtxt(Atom_1_1s, skiprows=1, usecols=[0])
Atom_1_1s_data = np.loadtxt(Atom_1_1s, skiprows=1, usecols=[2,3,4])
Atom_1_2p_data = np.loadtxt(Atom_1_2p, skiprows=1, usecols=[2,3,4])
Atom_2_1s_data = np.loadtxt(Atom_2_1s, skiprows=1, usecols=[2,3,4])
Atom_2_2p_data = np.loadtxt(Atom_2_2p, skiprows=1, usecols=[2,3,4])


size = len(energy_eV_data)
energy_1s = np.zeros(size)
energy_2p = np.zeros(size)

# ENERGY IN THE LEVEL 1s :

for i in range (0,3):
    energy_1s = energy_1s + Atom_1_1s_data[:,i] + Atom_2_1s_data[:,i]

# ENERGY IN THE LEVEL 2p :

for i in range (0,3):
    energy_2p = energy_2p + Atom_1_2p_data[:,i] + Atom_2_2p_data[:,i]

# Ploteamos

plt.plot(energy_eV_data, energy_1s, label = 'Si 1s' )
plt.plot(energy_eV_data, energy_2p, label = 'Si 2p' )
plt.xlabel('Energía[eV]')
plt.ylabel('PDOS')
plt.legend()
plt.show()