import numpy as np
import matplotlib.pyplot as plt

silicene_bands = 'silicene_bands.gnu'
fermi_energy = 1.7432

# Energía [eV]

energy_eV_data = np.loadtxt(silicene_bands, usecols=[0])
energy_eV_data = energy_eV_data + fermi_energy

# Points

points_eje_x = np.loadtxt(silicene_bands, usecols=[1])

# High simmetry points 

hs_point_1 = 0.0000
hs_point_2 = 0.5774
hs_point_3 = 0.9107
hs_point_4 = 1.5966

# Máxima y minima energía

max_energy = max(energy_eV_data)
min_energy = min(energy_eV_data)


# Ploteamos

plt.plot(points_eje_x, energy_eV_data, label = 'Estructura de bandas' )
plt.axvline(x=hs_point_1, ymin=min_energy, ymax=max_energy)
plt.axvline(x=hs_point_2, ymin=min_energy, ymax=max_energy)
plt.axvline(x=hs_point_3, ymin=min_energy, ymax=max_energy)
plt.axvline(x=hs_point_4, ymin=min_energy, ymax=max_energy)
plt.ylabel('Energía[eV]')
plt.title('ESTRUCTURA DE BANDAS DEL SILICENO')
plt.legend()
plt.show()