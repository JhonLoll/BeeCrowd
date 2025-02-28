def P1116():
    casos = int(input())

    for i in range(0, casos):
        X, Y = input().split(" ")
        X, Y = int(X), int(Y)

        if(X < 0 or Y == 0):
            print("divisao impossivel")
        elif(X == 0 and Y > 0):
            print(0.0)
        else:
            divisao = X/Y
            print(f'%.1f'%divisao)