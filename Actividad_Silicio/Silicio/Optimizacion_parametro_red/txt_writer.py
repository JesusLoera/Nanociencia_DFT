
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


a_i = 4.4

a_f = 6.4
dx = 0.1

directory = 'silicio'

n = int((a_f - a_i) / dx) 
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

    a = round(a_i + dx, 1)

    str_a = '  a= ' + str(a_i) + ','

    new_str_a = '  a= ' + str(a) + ','

    modificarLinea ( directory ,  str_a , new_str_a , i )
    modificarFuente( directory ,  str_a , new_str_a)

    a_i = round(a,1)
