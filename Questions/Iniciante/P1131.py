def P1131():
    def rept_opcao(opcao):
        if(opcao == 1):
            return 1
        elif(opcao < 1 or opcao > 2):
            return 0
        else:
            return 2

    inter, gremio = input().split(" ")
    inter, gremio = int(inter), int(gremio)

    gInter = empate = gGremio = 0

    grenal = 1

    while True:
        if(inter > gremio):
            gInter += 1
        elif(inter == gremio):
            empate += 1
        else:
            gGremio += 1
        opcao = int(input("Novo grenal (1-sim 2-nao)\n"))
        rept_opcao(opcao)

        if(rept_opcao(opcao) == 2):
            break
        elif(rept_opcao(opcao) == 0):
            rept_opcao(opcao)
        else:
            inter, gremio = input().split(" ")
            inter, gremio = int(inter), int(gremio)
            grenal += 1

    print(f'%i grenais'%grenal)
    print(f'Inter:%i'%gInter)
    print(f'Gremio:%i'%gGremio)
    print(f'Empates:%i'%empate)
    if(gGremio > gInter):
        print("Gremio venceu mais")
    else:
        print("Inter venceu mais")