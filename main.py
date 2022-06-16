from src.calculos import Calculos
from src.conf import inicio, final, incremento

if __name__ == '__main__':
    c = Calculos(inicio, final, incremento)
    c.calculadora(rango=False)