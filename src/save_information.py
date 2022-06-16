import os

from src.data import Data

path_files = 'Primos2'
csv_file = os.path.join(path_files, 'Informacion.csv')


def write_primes(file, data) -> None:
    """
    Agrega los numeros number_of_primes localizados al f, separandolos por espacios
    :param file: Nombre del archivo
    :param data: Lista de numeros number_of_primes
    :return:
    """
    file = os.path.join(path_files, file)

    with open(file, "w") as f:
        for e in data:
            f.write(str(e) + " ")


def export_information(data: Data):
    """
    Agrega una nueva linea a un fichero csv con informacion sobre el range de number_of_primes calculado
    :param data: Array con los data que se escribiran en el csv
    :return:
    """
    with open(csv_file, "a") as file:
        file.write(f"{data.__str__()}\n")
