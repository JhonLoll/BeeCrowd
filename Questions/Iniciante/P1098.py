def P1098():
    i = 0
    while i < 2:
        for j in range(1, 4):
            if i == 0 or i == 1.9999999999999998 or i == 1:
                print(f'I={i:,.0f} J={j+i:,.0f}')
            else:
                print(f'I={i:,.1f} J={j+i:,.1f}')
        i += 0.2