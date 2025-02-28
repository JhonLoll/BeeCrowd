def P1059():
    for i in range(1,101):
        if(i % 2) == 0:
            print(i)    

def P1060():
    positivo = 0
    for i in range(0,6):
        valor = float(input())
        if(valor > 0):
            positivo = positivo + 1
    print(f'%i valores positivos' %positivo)