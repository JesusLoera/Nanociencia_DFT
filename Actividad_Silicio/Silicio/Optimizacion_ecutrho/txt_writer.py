
# ELABORADO POR JESUS EDUARDO LOERA CASAS 1898887

def modificarLinea(archive,buscar,reemplazar,j):
        """
        Esta simple funcion cambia una linea entera de un archivo
        Tiene que recibir el nombre del archivo, la cadena de la linea entera a
        buscar, y la cadena a reemplazar si la linea coincide con buscar
        """
        
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


ecutwfc_i = 30
ecutrho_i = 30

k_ecutrho_i = 1
k_ecutrho_f = 12
dx = 1

directory = 'silicio'

n = (k_ecutrho_f - k_ecutrho_i)/dx + dx


for i in range (1,n+1):

    ecutrho = ecutwfc_i*i

    str_ecutrho = '  ecutrho = ' + str(ecutrho_i) + ','

    new_str_ecutrho = '  ecutrho = ' + str(ecutrho) + ','

    modificarLinea ( directory ,  str_ecutrho , new_str_ecutrho , i )
