import datetime
import os
import time

from .conf import path_files, csv_file
from .primos import listaPrimos


def write_primes(archivo, datos) -> None:
    '''
    Agrega los numeros primos localizados al fichero, separandolos por espacios
    :param archivo: Nombre del archivo
    :param datos: Lista de numeros primos
    :return:
    '''
    fichero = os.path.join(path_files, archivo)
    file = open(fichero, 'w')
    for e in datos:
        file.write(f'{e} ')
    file.close()


def create_files(range_title) -> dict:
    '''
    Agrega a un fichero csv informacion sobre el rango de numeros primos analizado
    :param range_title: rango de numeros primos con el formato <inicio a fin>
    :return: Array con los datos
    '''
    if not os.path.exists(path_files):
        os.mkdir(path_files)
    range_start, range_end = range_title.split('-')
    archivo = f"primos-{range_start}-{range_end}.txt"
    a = time.time()
    lista = listaPrimos(int(range_start), int(range_end))
    write_primes(archivo, lista)
    duracion = round(time.time() - a, 5)
    l = len(lista)
    return {"Rango": range_title, "Primos": l, "Duracion": duracion}


def print_info(fichero) -> None:
    '''
    Imprime en consola informacion sobre el avance de la creacion de ficheros
    :param fichero: Nombre del fichero
    :return: Impresion por pantalla con informacion sobre la hora y el nombre del fichero que se creara
    '''
    print(f'{time.strftime("%H.%M.%S", time.localtime())}  - Inicio de creacion de fichero de {fichero}')


def resume() -> None:
    '''
    Imprime en pantalla informacion sobre el fichero
    :return:
    '''
    file = open(csv_file)
    file.readline()
    nInicio = file.readline().split('-')[0]
    nFin = ""
    duracionS = float(0)
    nPrimos = 0
    nLineas = 1
    for e in file:
        nLineas += 1
        cont = e.rstrip().split(';')
        if cont[1].isdigit():
            nPrimos += int(cont[1])
            duracionS += float(cont[2].replace(',', '.'))
            nFin = cont[0].split('-')[1]

    print(
        f'Inicio: {nInicio}\nFin: {nFin}\nNº lineas: {nLineas}\nPrimos: {nPrimos}\nDuracion: {duracionS} seg.\t ({datetime.timedelta(seconds=duracionS)})')


def export_information(datos) -> None:
    '''
    Agrega una nueva linea a un fichero csv con informacion sobre el rango de primos calculado
    :param datos: Array con los datos que se escribiran en el csv
    :return:
    '''
    file = open(csv_file, "a")
    file.write(
        f"{datos['Rango']};{datos['Primos']};{datos['Duracion']}\n")
    file.close()
