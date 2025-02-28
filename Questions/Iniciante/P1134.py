def P1134():
    alcool = gasolina = diesel = 0
    while True:
        # 1.Álcool 2.Gasolina 3.Diesel 4.Fim
        tipo = int(input())

        if(tipo == 1):
            alcool += 1
        if(tipo == 2):
            gasolina += 1
        if(tipo == 3):
            diesel += 1
        if(tipo == 4):
            break
        else:
            continue

    print("MUITO OBRIGADO")
    print(f'Alcool: %i'%alcool)
    print(f'Gasolina: %i'%gasolina)
    print(f'Diesel: %i'%diesel)