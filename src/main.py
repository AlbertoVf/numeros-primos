from calculos import Calculos


def main():
    c = Calculos(
        inicio=62 * 100 * 1000 * 1000,
        final=63 * 100 * 1000 * 1000,
        incremento=1000 * 1000
    )
    c.continuar_calculos()


if __name__ == '__main__':
    main()