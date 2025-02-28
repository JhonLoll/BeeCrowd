def P1132():
    a = int(input())
    b = int(input())

    aux = 0
    soma = 0

    if(a > b):
        aux = a
        a = b
        b = aux

    for i in range(a, b+1):
        if(i % 13) != 0:
            soma += i
    print(soma)