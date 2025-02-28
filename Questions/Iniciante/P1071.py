def P1071():
    soma = 0

    X = int(input(""))
    Y = int(input(""))

    if X > Y:
        for i in range(Y + 1, X):
            if i % 2 != 0:
                soma = soma + i
    else:
        for i in range(X, Y):
            if i % 2 != 0:
                soma = soma + i

    print(soma)