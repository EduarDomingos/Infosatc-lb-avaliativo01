def Menu_Inicial():
    print("Conversor Milhas para quilometors")
    print("1. km/h para m/s")


def km_ms():
    M = float(input('Entre com o km/h: '))
    M = M/1.61
    print('Sua conversão foi de: {0}M/S'.format(M))
