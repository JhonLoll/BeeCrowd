def P1146():
    while True:
        x = int(input())

        if x == 0:
            break

        sequencia = ' '.join(map(str, range(1, x+1)))
        print(sequencia)