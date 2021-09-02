def Menu_Inicial():
    print ("programa para Conversão  de temperatura")
    print ("1. Converter  Celsius  para fahrenheit")

def fahr_cel():
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))


if __name__ == '__main__':
    Menu_Inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        fahr_cel()
