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
