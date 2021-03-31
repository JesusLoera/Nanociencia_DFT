
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



directory = 'silicano'
str_k_points = '2 2 1 0 0 0'
n = 20

for i in range (1,n+1):
    new_str_k_points= str(i) + ' ' + str(i) + ' ' + '1' + ' ' + '0 0 0'
    modificarLinea ( directory ,  str_k_points , new_str_k_points , i )
