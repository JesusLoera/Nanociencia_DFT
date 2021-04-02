import numpy as np
import matplotlib.pyplot as plt

Atom_1_H_1s = 'silicano_con_spin.pdos_atm#1(H)_wfc#1(s)'
Atom_2_Si_1s = 'silicano_con_spin.pdos_atm#2(Si)_wfc#1(s)'
Atom_2_Si_2p = 'silicano_con_spin.pdos_atm#2(Si)_wfc#2(p)'
Atom_3_Si_1s = 'silicano_con_spin.pdos_atm#3(Si)_wfc#1(s)'
Atom_3_Si_2p = 'silicano_con_spin.pdos_atm#3(Si)_wfc#2(p)'
Atom_4_H_1s = 'silicano_con_spin.pdos_atm#4(H)_wfc#1(s)'

energy_eV_data = np.loadtxt(Atom_1_H_1s, skiprows=1, usecols=[0])

Atom_1_H_1s_data = np.loadtxt(Atom_1_H_1s, skiprows=1, usecols=[1,2])
Atom_2_Si_1s_data = np.loadtxt(Atom_2_Si_1s, skiprows=1, usecols=[1,2])
Atom_2_Si_2p_data = np.loadtxt(Atom_2_Si_2p, skiprows=1, usecols=[1,2])
Atom_3_Si_1s_data = np.loadtxt(Atom_3_Si_1s, skiprows=1, usecols=[1,2])
Atom_3_Si_2p_data = np.loadtxt(Atom_3_Si_2p, skiprows=1, usecols=[1,2])
Atom_4_H_1s_data = np.loadtxt(Atom_4_H_1s, skiprows=1, usecols=[1,2])


# ENERGY IN THE LEVEL 1s :

energy_1s_up   = Atom_1_H_1s_data[:,0] + Atom_2_Si_1s_data[:,0] + Atom_3_Si_1s_data[:,0] + Atom_4_H_1s_data[:,0]
energy_1s_down = Atom_1_H_1s_data[:,1] + Atom_2_Si_1s_data[:,1] + Atom_3_Si_1s_data[:,1] + Atom_4_H_1s_data[:,1]

# ENERGY IN THE LEVEL 2p :

energy_2p_up   = Atom_2_Si_2p_data[:,0] + Atom_3_Si_2p_data[:,0]
energy_2p_down = Atom_2_Si_2p_data[:,1] + Atom_3_Si_2p_data[:,1]

# ENERGY H :

energy_H_up   = Atom_1_H_1s_data[:,0] + Atom_4_H_1s_data[:,0]
energy_H_down = Atom_1_H_1s_data[:,1] + Atom_4_H_1s_data[:,1]

# ENERGY Si :

energy_Si_up   =   Atom_2_Si_1s_data[:,0] + Atom_3_Si_1s_data[:,0] + Atom_2_Si_2p_data[:,0] + Atom_3_Si_2p_data[:,0]
energy_Si_down =   Atom_2_Si_1s_data[:,1] + Atom_3_Si_1s_data[:,1] + Atom_2_Si_2p_data[:,1] + Atom_3_Si_2p_data[:,1]

# TOTAL ENERGY:

total_energy_up   = energy_1s_up + energy_2p_up
total_energy_down = energy_1s_down + energy_2p_down


# Ploteamos por elemento UP

plt.plot(energy_eV_data, total_energy_up, label = 'Energía total' )
plt.plot(energy_eV_data, energy_H_up, label = 'H' )
plt.plot(energy_eV_data, energy_Si_up, label = 'Si' )
plt.xlabel('Energía[eV]')
plt.ylabel('PDOS')
plt.legend()
plt.grid()
plt.title('UP')
plt.show()

# Ploteamos por elemento UP

plt.plot(energy_eV_data, total_energy_up, label = 'Energía total' )
plt.plot(energy_eV_data, energy_H_down, label = 'H' )
plt.plot(energy_eV_data, energy_Si_down, label = 'Si' )
plt.xlabel('Energía[eV]')
plt.ylabel('PDOS')
plt.legend()
plt.grid()
plt.title('DOWN')
plt.show()

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