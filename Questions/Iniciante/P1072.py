def P1072():
    qtd = int(input())

    contadorIN = 0
    contadorOUT = 0

    while qtd > 0:
        valor = int(input())

        if(valor >= 10 and valor <= 20):
            contadorIN += 1
        else:
            contadorOUT += 1

        qtd -= 1

    print(f'%i in' %contadorIN)
    print(f'%i out' %contadorOUT)