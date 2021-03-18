
# ELABORADO POR JESÚS EDUARDO LOERA CASAS

import subprocess

def cmd(commando):
    subprocess.run(commando, shell=True)


ecutwfc_i = 20
ecutrho_i = 160

ecutwfc_f = 50
dx = 5

directory = 'silicio'
pwx = '/home/jesus/qe-6.6-ReleasePack/qe-6.6/bin/pw.x'

n = int((ecutwfc_f - ecutwfc_i) / dx)
n= n+2

for i in range (1,n):

    directory_aux = directory + '.' + str(i)
    input_aux = '<' + directory_aux + '.in' + '>' 
    output_aux = directory_aux + '.out' 


    comando_aux = pwx + ' ' + input_aux + ' ' + output_aux
    print(comando_aux)
    print('Ejecutando...')
    cmd(comando_aux)