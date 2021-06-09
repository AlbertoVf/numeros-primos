from src.informacion import create_files, export_information, print_info, csv_file

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

    def calculadora(self, rango: str = 'infinito') -> None:
        '''
        Crea ficheros .txt con los numeros primos comprendidos entre inicio y final. Cada fichero .txt tendra un rango desde inicio a inicio+incremento
        :param inicio: Numero por el que comienza a buscar los numeros primos
        :param final:  Ultimo numero que comprueba si es primo
        :param incremento: Rango de numeros que se introducira en el fichero
        :return: Fichero .txt con los numeros primos
        '''
        if rango == 'rango':
            while (self.inicio < self.final):
                self.calc()
                self.inicio += self.incremento
        elif rango == 'infinito':
            while (True):
                self.calc()
                self.inicio += self.incremento

    def continuar_calculos(self) -> None:
        '''
        Calcula los numeros primos a partir del ultimo rango que hay en el fichero
        :param final:  Ultimo numero que comprueba si es primo
        :param incremento: Rango de numeros que se introducira en el fichero
        :return:
        '''
        file = open(csv_file)
        for e in file:
            cont = e.rstrip().split(';')
            if cont[1].isdigit():
                i = cont[0].split('-')[1]
        i = int(i)
        while (i < self.final):
            self.calc()
            i += self.incremento
