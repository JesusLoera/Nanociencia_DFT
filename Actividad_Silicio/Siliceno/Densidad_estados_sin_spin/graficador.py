import numpy as np
import matplotlib.pyplot as plt

Atom_1_1s = 'test.pdos_atm#1(Si)_wfc#1(s)'
Atom_1_2p = 'test.pdos_atm#1(Si)_wfc#2(p)'
Atom_2_1s = 'test.pdos_atm#2(Si)_wfc#1(s)'
Atom_2_2p = 'test.pdos_atm#2(Si)_wfc#2(p)'

energy_eV_data = np.loadtxt(Atom_1_1s, skiprows=1, usecols=[0])
Atom_1_1s_data = np.loadtxt(Atom_1_1s, skiprows=1, usecols=[1,2])
Atom_1_2p_data = np.loadtxt(Atom_1_2p, skiprows=1, usecols=[1,2])
Atom_2_1s_data = np.loadtxt(Atom_2_1s, skiprows=1, usecols=[1,2])
Atom_2_2p_data = np.loadtxt(Atom_2_2p, skiprows=1, usecols=[1,2])


size = len(energy_eV_data)
energy_1s = np.zeros(size)
energy_2p = np.zeros(size)


# ENERGY IN THE LEVEL 1s :

energy_1s_up   = Atom_1_1s_data[:,0] + Atom_2_1s_data[:,0]
energy_1s_down = Atom_1_1s_data[:,1] + Atom_2_1s_data[:,1]

# ENERGY IN THE LEVEL 2p :

energy_2p_up   = Atom_1_2p_data[:,0] + Atom_2_2p_data[:,0]
energy_2p_down = Atom_1_2p_data[:,1] + Atom_2_2p_data[:,1]

# TOTAL ENERGY :

total_energy_up   = energy_1s_up + energy_2p_up
total_energy_down = energy_1s_down + energy_2p_down

# Ploteamos UP

plt.plot(energy_eV_data, total_energy_up, label = 'Energía total' )
plt.plot(energy_eV_data, energy_1s_up, label = 'Energía en 1s' )
plt.plot(energy_eV_data, energy_2p_up, label = 'Energía en 2p' )
plt.xlabel('Energía[eV]')
plt.ylabel('PDOS')
plt.legend()
plt.grid()
plt.title('UP')
plt.show()


# Ploteamos DOWN

plt.plot(energy_eV_data, total_energy_down, label = 'Energía total' )
plt.plot(energy_eV_data, energy_1s_down, label = 'Energía en 1s' )
plt.plot(energy_eV_data, energy_2p_down, label = 'Energía en 2p' )
plt.xlabel('Energía[eV]')
plt.ylabel('PDOS')
plt.legend()
plt.grid()
plt.title('DOWN')
plt.show()