def P1094():
    casos = int(input())

    coelho, sapo, rato, total= 0,0,0,0

    for i in range(0, casos):
        qtdAnimal, animal = input().split(" ")

        qtdAnimal = int(qtdAnimal)

        total += qtdAnimal

        if(animal == 'C'):
            coelho += qtdAnimal
        elif(animal == 'S'):
            sapo += qtdAnimal
        else:
            rato += qtdAnimal

    porctC = (coelho * 100) / total
    porctS = (sapo * 100) / total
    porctR = (rato * 100) / total

    print(porctC)

    print(f'TOTAL: %i cobaias' %total)
    print(f'Total de coelhos: %i' %coelho)
    print(f'Total de ratos: %i' %rato)
    print(f'Total de sapos: %i' %sapo)
    print(f'Percentual de coelhos: %.2f' %porctC + ' %')
    print(f'Percentual de ratos: %.2f' %porctR + ' %')
    print(f'Percentual de sapos: %.2f' %porctS + ' %')