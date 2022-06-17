import os

from src.data import Data

path_files = 'Primos'
csv_file = os.path.join(path_files, 'Informacion.csv')


def write_primes(file, data):
    """
    Write primes to file
    :param file: File to write
    :param data: Primes to write
    """
    file = os.path.join(path_files, file)

    with open(file, "w") as f:
        for e in data:
            f.write(str(e) + " ")


def export_information(data: Data):
    """
    Export information to csv file
    :param data: Information to export
    """
    with open(csv_file, "a") as file:
        file.write(f"{data.__str__()}\n")


def read_information():
    import datetime

    """
    Read information from csv file
    :return: Information
    """
    dat: [Data] = []
    with open(f'{csv_file}', "r") as file:
        lines = file.readlines()

    for l in lines[1:]:
        dat.append(Data(l.split(';')[0], int(l.split(';')[1]), float(l.split(';')[2])))

    primos = 0
    tiempo = 0

    for d in dat:
        primos += d.number_of_primes
        tiempo += d.duration

    info = {
        'rangos': len(dat),
        'primos': primos,
        'tiempo': str(datetime.timedelta(seconds=tiempo))
    }
    print(info)

# read_information()
