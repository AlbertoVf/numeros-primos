from .informacion import create_files, export_information, print_info


class Calculos:

    def __init__(self, inicio: int, final: int, incremento=1000 * 1000):
        self.incremento = incremento
        self.inicio = inicio
        self.final = final

    def calc(self):
        fichero = f'{self.inicio}-{self.inicio + self.incremento}'
        print_info(fichero)
        cf = create_files(fichero)
        export_information(cf)

    def calculadora(self, rango: bool = True) -> None:
        '''
        Establece el rango de calculos. False indica que el rango es infinito. True calcula con los limites establecidos
        '''
        if rango:
            while (self.inicio < self.final):
                self.calc()
                self.inicio += self.incremento
        else:
            while (True):
                self.calc()
                self.inicio += self.incremento
