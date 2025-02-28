def P1079():
    cont = int(input())

    peso2 = 2
    peso3 = 3
    peso5 = 5

    while cont > 0:
        a, b, c = input().split(" ")

        a = float(a)
        b = float(b)
        c = float(c)

        media = ((a*peso2)+(b*peso3)+(c*peso5))/(peso2+peso3+peso5)

        print(f'%.1f' %media)

        cont -= 1