
# ELABORADO POR JESUS EDUARDO LOERA CASAS 1898887

def modificarLinea(archive,buscar,reemplazar,j):
        """
        Esta simple funcion cambia una linea entera de un archivo
        Tiene que recibir el nombre del archivo, la cadena de la linea entera a
        buscar, y la cadena a reemplazar si la linea coincide con buscar
        """

        j = j+1
        
        new_archive = archive + '.' + str(j) + '.in'

        archive = archive + '.in'

        """
        Primero reescribir todo el nuevo archivo.
        """

        f = open(archive, "r")
        information = f.read()

        g = open(new_archive, "w")
        g.write(information)
    
        with open(archive, "r") as f:
            # obtenemos las lineas del archivo en una lista
            lines = (line.rstrip() for line in f)
    
            # busca en cada linea si existe la cadena a buscar, y si la encuentra
            # la reemplaza
            altered_lines = [reemplazar if line==buscar else line for line in lines]
    
        with open(new_archive, "w") as g:
            # guarda nuevamente todas las lineas en el archivo
            g.write('\n'.join(altered_lines) + '\n')

def modificarFuente(archive,buscar,reemplazar):
        """
        Esta simple funcion cambia una linea entera de un archivo
        Tiene que recibir el nombre del archivo, la cadena de la linea entera a
        buscar, y la cadena a reemplazar si la linea coincide con buscar
        """

        archive = archive + '.in'

        f = open(archive, "r")
    
        with open(archive, "r") as f:
            # obtenemos las lineas del archivo en una lista
            lines = (line.rstrip() for line in f)
    
            # busca en cada linea si existe la cadena a buscar, y si la encuentra
            # la reemplaza
            altered_lines = [reemplazar if line==buscar else line for line in lines]
    
        with open(archive, "w") as f:
            # guarda nuevamente todas las lineas en el archivo
            f.write('\n'.join(altered_lines) + '\n')


ecutwfc_i = 20
ecutrho_i = 160

ecutwfc_f = 50
dx = 5

directory = 'silicio'

n = int((ecutwfc_f - ecutwfc_i) / dx)
n= n+1


"""
Copiamos el original
"""

f = open(directory+'.in', "r")
information = f.read()

g = open(directory+'.1.in', "w")
g.write(information)

"""
Creamos los demas txt
"""

for i in range (1,n):

    ecutwfc = ecutwfc_i + dx
    ecutrho = ecutwfc*8

    str_ecutwfc = '  ecutwfc = ' + str(ecutwfc_i) + ','
    str_ecutrho = '  ecutrho = ' + str(ecutrho_i) + ','

    new_str_ecutwfc = '  ecutwfc = ' + str(ecutwfc) + ','
    new_str_ecutrho = '  ecutrho = ' + str(ecutrho) + ','

    modificarLinea ( directory ,  str_ecutwfc , new_str_ecutwfc , i )
    modificarFuente( directory ,  str_ecutwfc , new_str_ecutwfc)
    modificarLinea ( directory ,  str_ecutrho , new_str_ecutrho , i )
    modificarFuente( directory ,  str_ecutrho , new_str_ecutrho)

    ecutwfc_i = ecutwfc
    ecutrho_i = ecutrho

    