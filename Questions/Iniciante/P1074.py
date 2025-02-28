def P1074():
# ODD NEGATIVE --> impar negativo
# NULL --> 0
# ODD POSITIVE --> impar positivo
# EVEN NEGATIVE --> par negativo 

    qtd = int(input())

    for i in range(1, qtd+1):
        valor = int(input())
        if(valor == 0):
            print("NULL")
        elif((valor % 2) == 0 and valor < 0):
            print("EVEN NEGATIVE")
        elif((valor % 2) == 0 and valor > 0):
            print("EVEN POSITIVE")
        elif((valor % 2) != 0 and valor < 0):
            print("ODD NEGATIVE")
        elif((valor % 2) != 0 and valor > 0):
            print("ODD POSITIVE")