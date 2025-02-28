def P1149():
    while True:
        entrada = input().split()
        a = int(entrada[0])
        n = int(entrada[-1])
        if n <= 0:
            break
        soma = 0
        for i in range(n):
            soma += a + i
        print(soma)
P1149()