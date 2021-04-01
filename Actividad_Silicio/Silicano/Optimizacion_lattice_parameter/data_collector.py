
# PROGRAMA ELABORADO POR JESUS EDUARDO LOERA CASAS

import re
import numpy as np

def collector(archivo, line_energy):

    DATA=np.array([])

    for i in range (1,22):

        archivo_aux = archivo + '.' + str(i) + '.out'

        resultado = []
        with open(archivo_aux) as f:
            for linea in f:
                if linea.startswith(line_energy):
                    resultado = []       # Borrar lo que hubiera acumulado
                resultado.append(linea)  # Añadir la última línea leida
        temp_string = resultado[0]
        t_energy = [float(s) for s in re.findall(r'-?\d+\.?\d*', temp_string)]
        DATA = np.append( DATA, t_energy[0] )

    return DATA

archivo = 'silicano'

line_energy = '!    total energy              =     '

DATA = collector(archivo, line_energy)



print(len(DATA))
print(DATA)