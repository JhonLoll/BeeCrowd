def P1144():
    x = int(input())

    for i in range(1, x + 1):
        print(f'{i} {i ** 2} {i ** 3}')
        print(f'{i} {i ** 2 + 1} {i ** 3 + 1}')