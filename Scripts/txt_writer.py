
# ELABORADO POR JESÚS EDUARDO LOERA CASAS 1898887

def modificarLinea(archivo,buscar,reemplazar,i):
	"""
	Esta simple función cambia una linea entera de un archivo
	Tiene que recibir el nombre del archivo, la cadena de la linea entera a
	buscar, y la cadena a reemplazar si la linea coincide con buscar
	"""

    i=i+1

    archive = archive + '.in'

    new_archive = archive + f'{i}' + '.in'

    """
    Primero reescribir todo el nuevo archivo.
    """

    f = open(archive, "r")
    information = f.read()

    g = open(new_archive, "w")
    g.write(information")
 
	with open(archive, "r") as f:
		# obtenemos las lineas del archivo en una lista
		lines = (line.rstrip() for line in f)
 
		# busca en cada linea si existe la cadena a buscar, y si la encuentra
		# la reemplaza
		altered_lines = [reemplazar if line==buscar else line for line in lines]
 
	with open(archivo, "w") as f:
		# guarda nuevamente todas las lineas en el archivo
		g.write('\n'.join(altered_lines) + '\n')


ecutwfc_i = 20
ecutrho_i = 160

ecutwfc_f = 50
dx = 5

n = (ecutwfc_f - ecutwfc_i)/dx 
n= n+1

for i in range (n):

    ecutwfc = ecutwfc_i + i*dx
    ecutrho = ecutwfc*8

    modificarLinea( ,  f'  ecutwfc = {ecutwfc_i},', f'  ecutwfc = {ecutwfc},')
    modificarLinea( ,  f'  ecutrho = {ecutwfc_i},', f'  ecutwfc = {ecutrho},')