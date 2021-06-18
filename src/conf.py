import os
path_files = 'Primos'
csv_file = os.path.join(path_files, 'Informacion.csv')


def ultimo_calculo():
    archivos = len(os.listdir(path_files))-1
    return archivos * incremento


incremento = 1000 * 1000
inicio = ultimo_calculo()
final = inicio * 100
