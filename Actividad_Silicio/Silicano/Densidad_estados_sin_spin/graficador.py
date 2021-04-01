import numpy as np
import matplotlib.pyplot as plt

Atom_1_H_1s = 'silicano.pdos_atm#1(H)_wfc#1(s)'
Atom_2_Si_1s = 'silicano.pdos_atm#2(Si)_wfc#1(s)'
Atom_2_Si_2p = 'silicano.pdos_atm#2(Si)_wfc#2(p)'
Atom_3_Si_1s = 'silicano.pdos_atm#3(Si)_wfc#1(s)'
Atom_3_Si_2p = 'silicano.pdos_atm#3(Si)_wfc#2(p)'
Atom_4_H_1s = 'silicano.pdos_atm#4(H)_wfc#1(s)'

energy_eV_data = np.loadtxt(Atom_1_H_1s, skiprows=1, usecols=[0])

Atom_1_H_1s_data = np.loadtxt(Atom_1_H_1s, skiprows=1, usecols=[2,3,4])
Atom_2_Si_1s_data = np.loadtxt(Atom_2_Si_1s, skiprows=1, usecols=[2,3,4])
Atom_2_Si_2p_data = np.loadtxt(Atom_2_Si_2p, skiprows=1, usecols=[2,3,4])
Atom_3_Si_1s_data = np.loadtxt(Atom_3_Si_1s, skiprows=1, usecols=[2,3,4])
Atom_3_Si_2p_data = np.loadtxt(Atom_3_Si_2p, skiprows=1, usecols=[2,3,4])
Atom_4_H_1s_data = np.loadtxt(Atom_4_H_1s, skiprows=1, usecols=[2,3,4])

size = len(energy_eV_data)
energy_1s = np.zeros(size)
energy_2p = np.zeros(size)

# ENERGY IN THE LEVEL 1s :

for i in range (0,3):
    energy_1s = energy_1s + Atom_1_H_1s_data[:,i]  + Atom_2_Si_1s_data[:,i] + Atom_3_Si_1s_data[:,i] + Atom_4_H_1s_data[:,i] 

# ENERGY IN THE LEVEL 2p :

for i in range (0,3):
    energy_2p = energy_2p + Atom_2_Si_2p_data[:,i] + Atom_3_Si_2p_data[:,i]

# Ploteamos

plt.plot(energy_eV_data, energy_1s, label = 'Si 1s' )
plt.plot(energy_eV_data, energy_2p, label = 'Si 2p' )
plt.xlabel('Energía[eV]')
plt.ylabel('PDOS')
plt.legend()
plt.show()