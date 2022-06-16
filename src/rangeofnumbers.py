import os
import time

from src.data import Data
from src.prime import prime_list
from src.save_information import path_files, export_information, write_primes


class RangeOfNumbers:
    log = Data()

    def __init__(self, start: int = 0, final: int = 100 * 1000 * 1000):
        self.start = start
        self.final = final
        self.file = f'{self.start}-{self.final}'

    def calculate(self):
        a = time.time()
        self.create_files()
        b = time.time()
        self.log.__dict__.update({'duration': round(b - a, 5)})
        export_information(self.log)

    def create_files(self):
        if not os.path.exists(path_files):
            os.mkdir(path_files)
        range_start, range_end = self.file.split('-')
        list = prime_list(int(range_start), int(range_end))
        write_primes(f"numeros_primos-{range_start}-{range_end}.txt", list)

        self.log.__dict__.update({'range': self.file, 'number_of_primes': len(list)})

    def __str__(self):
        return f'Calculos: inicio: {self.start}, final: {self.final}'
