def P1065():
    par = 0
    impar = 0
    positivo = 0
    negativo = 0

    for i in range(0,5):
        valor = int(input())
        if(valor % 2) == 0:
            par += 1
        else:
            impar += 1
        if(valor > 0):
            positivo += 1
        if(valor < 0):
            negativo += 1
    print(f'%i valor(es) par(es)' %par)
    print(f'%i valor(es) impar(es)' %impar)
    print(f'%i valor(es) positivo(s)' %positivo)
    print(f'%i valor(es) negativo(s)' %negativo)