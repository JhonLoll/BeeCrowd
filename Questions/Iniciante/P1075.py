def P1075():
    divisor = int(input())

    for i in range (0, 10000):
        if(i % divisor) == 2:
            print(i)