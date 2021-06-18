from src.calculos import Calculos


if __name__ == '__main__':
    c = Calculos(
        inicio=0,
        final=100 * 1000 * 1000,
        incremento=1000 * 1000
    )
    c.calculadora(rango=True)
