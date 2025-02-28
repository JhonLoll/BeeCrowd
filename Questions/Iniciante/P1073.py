def P1073():
    valor = int(input())

    for i in range(1, valor+1):
        if(i % 2) == 0:
            print(f'%i^2 ='%i, i*i)