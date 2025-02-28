def P1118():
    def novo_calculo(valor):
        if(valor == 1):
            return 1
        elif(valor < 1 or valor > 2):
            return 2
        else:
            return 0
    def verf_nota(nota):
        if(nota < 0 or nota > 10):
            print("nota invalida")
        else:
            return 0

    while True:
        while True:
            nota1 = float(input())
            if(verf_nota(nota1) == 0):
                break
        while True:
            nota2 = float(input())
            if(verf_nota(nota2) == 0):
                break
        media = (nota1+nota2)/2
        print(f'media = %.2f'%media)

        while True:
            opcao = int(input("novo calculo (1-sim 2-nao)\n"))
            if(novo_calculo(opcao) == 0):
                break
            elif(novo_calculo(opcao) == 2):
                novo_calculo(opcao)
            else:
                while True:
                    nota1 = float(input())
                    if(verf_nota(nota1) == 0):
                        break
                while True:
                    nota2 = float(input())
                    if(verf_nota(nota2) == 0):
                        break
                media = (nota1+nota2)/2
                print(f'media = %.2f'%media)
        break