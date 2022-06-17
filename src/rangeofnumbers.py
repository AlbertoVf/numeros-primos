import os
import time

from src.data import Data
from src.prime import prime_list
from src.save_information import path_files, export_information, write_primes


class RangeOfNumbers:
    data = Data()

    def __init__(self, start: int = 0, final: int = None):
        self.increment = 1 * 1000 * 1000
        self.start = start
        self.final = final if final else start + self.increment
        self.file = f'{self.start}-{self.final}'

    def calculate(self):
        a = time.time()
        self.create_files()
        b = time.time()
        self.data.__dict__.update({'duration': round(b - a, 5)})
        export_information(self.data)

    def create_files(self):
        if not os.path.exists(path_files):
            os.mkdir(path_files)
        range_start, range_end = self.file.split('-')
        list = prime_list(int(range_start), int(range_end))
        write_primes(f"primos-{range_start}-{range_end}.txt", list)

        self.data.__dict__.update({'range': self.file, 'number_of_primes': len(list)})

    def __str__(self):
        return f'start: {self.start}, end: {self.final}, file: {self.file}'
