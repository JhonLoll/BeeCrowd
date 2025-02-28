def P1113():
    while True:
        X, Y = input().split(" ")
        X, Y = int(X), int(Y)

        if(X == Y):
            break
        if(X > Y):
            print("Decrescente")
        else:
            print("Crescente")