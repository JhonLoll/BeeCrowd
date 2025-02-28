def P1101():
    while True:
        aux = 0
        soma = 0
        M, N = input().split(" ")
        M, N = int(M), int(N)

        if(M <= 0 or N <= 0):
            break
        if(M > N):
            aux = M
            M = N
            N = aux
        for i in range(M, N+1):
            soma += i
            print(f'{i}', end=" ")
        print(f'Sum={soma}')