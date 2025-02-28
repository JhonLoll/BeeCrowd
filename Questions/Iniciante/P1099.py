def P1099():
    casos = int(input())
    aux = 0
    for i in range(0, casos):
        soma = 0
        inicio, fim = input().split(" ")
        inicio, fim = int(inicio), int(fim)

        if(inicio > fim):
            aux = inicio
            inicio = fim
            fim = aux
        for x in range(inicio+1, fim):
            if(x % 2) != 0:
                soma += x
    print(soma)