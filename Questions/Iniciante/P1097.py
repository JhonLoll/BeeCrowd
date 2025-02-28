def P1097():
    for i in range(1, 10, 2):
        j1 = i + 6
        j = j1
        for x  in range(0, 3):
            print(f'I={i} J={j}')
            j -= 1