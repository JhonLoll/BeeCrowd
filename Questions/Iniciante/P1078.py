def P1078():
    valor = int(input())

    for i in range(1, 11):
        mult = i*valor
        output = "{0} x {1} = {2}".format(i, valor, mult)
        print(output)