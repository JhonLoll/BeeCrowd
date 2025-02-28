def P1142():
    linhas = int(input("Insira a quantidade de linhas: "))
    j = 1
    for i in range(0, linhas):
        print(f'{j} {j+1} {j+2} PUM')
        j+=4