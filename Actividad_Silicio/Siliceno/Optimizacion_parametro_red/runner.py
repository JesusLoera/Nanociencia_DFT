
# ELABORADO POR JESÚS EDUARDO LOERA CASAS

import subprocess

def cmd(commando):
    subprocess.run(commando, shell=True)



directory = 'siliceno_second'
pwx = '/home/jesus/qe-6.6-ReleasePack/qe-6.6/bin/pw.x'


for i in range (1,12):
 
    directory_aux = directory + '.' + str(i)
    input_aux = '<' + directory_aux + '.in' + '>' 
    output_aux = directory_aux + '.out' 


    comando_aux = pwx + ' ' + input_aux + ' ' + output_aux
    print(comando_aux)
    print('Ejecutando...')
    cmd(comando_aux)