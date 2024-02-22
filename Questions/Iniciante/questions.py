import numpy as np
#? QUESTÕES RESOLVIDAS
# P1046() P1051() P1052() P1059() P1060() P1064() P1065() P1067() P1070()
# P1071() P1072() P1073() P1074() P1075() P1078() P1079() P1080() P1094()
# P1095() P1096() P1097() P1098() P1099() P1101() P1113() P1114() P1115()
# P1115() P1116() P1118() P1131() P1132() P1134() P1143()
#! QUESTÃO INCOMPLETA
#! P1051()


def P1046():
    
    #? Tempo de Jogo
    
    inicio, fim = input().split(" ")

    inicio, fim = int(inicio), int(fim)

    if(inicio == fim):
        hora = 24
    if(inicio > fim):
        hora = 24 - (inicio - fim)
    if(inicio < fim):
        hora = (24 - inicio) - (24 - fim)
        
    print(f'O JOGO DUROU {hora} HORA(S)')

def P1051():
    salario = float(input("Insira seu salário: "))

    if salario <= 2000:
        print("Isento")
    elif salario > 2000:
        if salario <= 3000:
            salario = salario - 1000
            imposto = salario * (8/100)
            if salario <= 3500:
                salario = salario - 1500
                imposto = imposto + (salario * (18/100))
                if salario > 3500:
                    imposto = imposto + (salario * (25/100))
    print(imposto)

def P1052():
    mes = int(input(""))

    if(mes == 1):
        print("January")
    if(mes == 2):
        print("February")
    if(mes == 3):
        print("March")
    if(mes == 4):
        print("April")
    if(mes == 5):
        print("May")
    if(mes == 6):
        print("June")
    if(mes == 7):
        print("July")
    if(mes == 8):
        print("August")
    if(mes == 9):
        print("September")
    if(mes == 10):
        print("October")
    if(mes == 11):
        print("November")
    if(mes == 12):
        print("December")

def P1059():
    for i in range(1,101):
        if(i % 2) == 0:
            print(i)    

def P1060():
    positivo = 0
    for i in range(0,6):
        valor = float(input())
        if(valor > 0):
            positivo = positivo + 1
    print(f'%i valores positivos' %positivo)

def P1064():
    positivo = 0
    soma = 0
    for i in range(0,6):
        valor = float(input())
        if(valor > 0):
            positivo = positivo + 1
            soma += valor
    media = soma/positivo
    print(f'%i valores positivos' %positivo)
    print(f'%.1f' %media)

def P1065():
    par = 0
    impar = 0
    positivo = 0 
    negativo = 0

    for i in range(0,5):
        valor = int(input())
        if(valor % 2) == 0:
            par += 1
        else:
            impar += 1
        if(valor > 0):
            positivo += 1
        if(valor < 0):
            negativo += 1
    print(f'%i valor(es) par(es)' %par)
    print(f'%i valor(es) impar(es)' %impar)
    print(f'%i valor(es) positivo(s)' %positivo)
    print(f'%i valor(es) negativo(s)' %negativo)

def P1067():
    fim = int(input())

    for i in range(0,fim+1):
        if(i % 2) != 0:
            print(i)

def P1070():
    X = int(input())

    for i in range(X, X+12):
        if(i % 2) != 0:
            print(i)
        
def P1071():
    soma = 0

    X = int(input(""))
    Y = int(input(""))

    if X > Y:
        for i in range(Y + 1, X):
            if i % 2 != 0:
                soma = soma + i
    else:
        for i in range(X, Y):
            if i % 2 != 0:
                soma = soma + i

    print(soma)

def P1072():
    qtd = int(input())

    contadorIN = 0
    contadorOUT = 0

    while qtd > 0:
        valor = int(input())
        
        if(valor >= 10 and valor <= 20):
            contadorIN += 1
        else:
            contadorOUT += 1

        qtd -= 1

    print(f'%i in' %contadorIN)
    print(f'%i out' %contadorOUT)

def P1073():
    valor = int(input())

    for i in range(1, valor+1):
        if(i % 2) == 0:
            print(f'%i^2 ='%i, i*i)

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

def P1075():
    divisor = int(input())

    for i in range (0, 10000):
        if(i % divisor) == 2:
            print(i)

def P1078():
    valor = int(input())

    for i in range(1, 11):
        mult = i*valor
        output = "{0} x {1} = {2}".format(i, valor, mult)
        print(output)

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
def P1080():
    maior = 0
    posicao = 0
    for i in range(0,100):
        valor = int(input())
        if(valor > maior):
            maior =  valor
            posicao = i+1
    print(maior)
    print(posicao)

def P1094():
    casos = int(input())

    coelho, sapo, rato, total= 0,0,0,0

    for i in range(0, casos):
        qtdAnimal, animal = input().split(" ")
        
        qtdAnimal = int(qtdAnimal)
        
        total += qtdAnimal
        
        if(animal == 'C'):
            coelho += qtdAnimal
        elif(animal == 'S'):
            sapo += qtdAnimal
        else:
            rato += qtdAnimal
        
    porctC = (coelho * 100) / total
    porctS = (sapo * 100) / total
    porctR = (rato * 100) / total

    print(porctC)

    print(f'TOTAL: %i cobaias' %total)
    print(f'Total de coelhos: %i' %coelho)
    print(f'Total de ratos: %i' %rato)
    print(f'Total de sapos: %i' %sapo)
    print(f'Percentual de coelhos: %.2f' %porctC + ' %')
    print(f'Percentual de ratos: %.2f' %porctR + ' %')
    print(f'Percentual de sapos: %.2f' %porctS + ' %')

def P1095():
    i = 1
    for j in range(60, -5, -5):
        print(f'I={i} J={j}')
        i += 3
        
def P1096():
    for i in range(1, 10, 2):
        j = 7
        while (j >= 5):
            print(f'I={i} J={j}')
            j -= 1
            
def P1097():
    for i in range(1, 10, 2):
        j1 = i + 6
        j = j1
        for x  in range(0, 3): 
            print(f'I={i} J={j}')
            j -= 1
def P1098():
    i = 0
    while i < 2:
        for j in range(1, 4):
            if i == 0 or i == 1.9999999999999998 or i == 1:
                print(f'I={i:,.0f} J={j+i:,.0f}')
            else:
                print(f'I={i:,.1f} J={j+i:,.1f}')
        i += 0.2

def P1099():
    casos = int(input())
    aux = 0
    for i in range(0, casos):
        soma = 0
        inicio, fim = input().split(" ")
        inicio, fim = int(inicio), int(fim)
        
        if(inicio > fim):
            aux = inicio
            inicio = fim
            fim = aux 
        for x in range(inicio+1, fim):
            if(x % 2) != 0:
                soma += x
    print(soma)

def P1101():
    while True:
        aux = 0
        soma = 0
        M, N = input().split(" ")
        M, N = int(M), int(N)
        
        if(M <= 0 or N <= 0):
            break
        if(M > N):
            aux = M
            M = N
            N = aux
        for i in range(M, N+1):
            soma += i
            print(f'{i}', end=" ")
        print(f'Sum={soma}')

def P1113():
    while True:
        X, Y = input().split(" ")
        X, Y = int(X), int(Y)
        
        if(X == Y):
            break
        if(X > Y):
            print("Decrescente")
        else:
            print("Crescente")

def P1114():
    while True:
        tentativa = int(input())
        
        if(tentativa != 2002):
            print("Senha Invalida")
        else:
            print("Acesso Permitido")
            break

def P1115():
    while True:
        X, Y = input().split()
        X, Y = int(X), int(Y)
        
        if(X == 0 or Y == 0):
            break
        if(X > 0 and Y > 0):
            print("primeiro")
        elif(X < 0 and Y > 0):
            print("segundo")
        elif(X > 0 and Y < 0):
            print("quarto")
        else:
            print("terceiro")

def P1116():
    casos = int(input())

    for i in range(0, casos):
        X, Y = input().split(" ")
        X, Y = int(X), int(Y)

        if(X < 0 or Y == 0):
            print("divisao impossivel")
        elif(X == 0 and Y > 0):
            print(0.0)
        else:
            divisao = X/Y
            print(f'%.1f'%divisao)

def P1118():
    def novo_calculo(valor):
        if(valor == 1):
            return 1
        elif(valor < 1 or valor > 2):
            return 2
        else:
            return 0
    def verf_nota(nota):
        if(nota < 0 or nota > 10):
            print("nota invalida")
        else:
            return 0
        
    while True:
        while True:
            nota1 = float(input())
            if(verf_nota(nota1) == 0):
                break
        while True:
            nota2 = float(input())
            if(verf_nota(nota2) == 0):
                break
        media = (nota1+nota2)/2
        print(f'media = %.2f'%media)
        
        while True:
            opcao = int(input("novo calculo (1-sim 2-nao)\n"))
            if(novo_calculo(opcao) == 0):
                break
            elif(novo_calculo(opcao) == 2):
                novo_calculo(opcao)
            else:
                while True:
                    nota1 = float(input())
                    if(verf_nota(nota1) == 0):
                        break
                while True:
                    nota2 = float(input())
                    if(verf_nota(nota2) == 0):
                        break
                media = (nota1+nota2)/2
                print(f'media = %.2f'%media)
        break
    
def P1131():
    def rept_opcao(opcao):
        if(opcao == 1):
            return 1
        elif(opcao < 1 or opcao > 2):
            return 0
        else:
            return 2
            
    inter, gremio = input().split(" ")
    inter, gremio = int(inter), int(gremio)

    gInter = empate = gGremio = 0

    grenal = 1

    while True:
        if(inter > gremio):
            gInter += 1
        elif(inter == gremio):
            empate += 1
        else:
            gGremio += 1
        opcao = int(input("Novo grenal (1-sim 2-nao)\n"))
        rept_opcao(opcao)
        
        if(rept_opcao(opcao) == 2):
            break
        elif(rept_opcao(opcao) == 0):
            rept_opcao(opcao)
        else:
            inter, gremio = input().split(" ")
            inter, gremio = int(inter), int(gremio)
            grenal += 1

    print(f'%i grenais'%grenal)
    print(f'Inter:%i'%gInter)
    print(f'Gremio:%i'%gGremio)
    print(f'Empates:%i'%empate)
    if(gGremio > gInter):
        print("Gremio venceu mais")
    else:
        print("Inter venceu mais")

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

def P1134():
    alcool = gasolina = diesel = 0
    while True:
        # 1.Álcool 2.Gasolina 3.Diesel 4.Fim
        tipo = int(input())
        
        if(tipo == 1):
            alcool += 1
        if(tipo == 2):
            gasolina += 1
        if(tipo == 3):
            diesel += 1
        if(tipo == 4):
            break
        else:
            continue
        
    print("MUITO OBRIGADO")
    print(f'Alcool: %i'%alcool)
    print(f'Gasolina: %i'%gasolina)
    print(f'Diesel: %i'%diesel)

def P1142():
    linhas = int(input("Insira a quantidade de linhas: "))
    j = 1
    for i in range(0, linhas):
        print(f'{j} {j+1} {j+2} PUM')
        j+=4

def P1143():
    linhas = int(input())

    for i in range(1, linhas+1):
        print(f'{i} {i*i} {i*i*i}')
        
def P1047():
    horaI, minutoI, horaF, minutoF = input().split(" ")
    horaI, minutoI, horaF, minutoF = int(horaI), int(minutoI), int(horaF), int(minutoF)
    
    if horaI < horaF:
        hora = horaF - horaI
        if minutoI < minutoF:
            minuto = minutoF - minutoI
        if minutoI > minutoF:
            hora -= 1
            minuto = (60 - minutoI) + minutoF
        if minutoI == minutoF:
            minuto = 0

    if horaI > horaF:
        hora = (24 - horaI) + horaF
        if minutoI < minutoF:
            minuto = minutoF - minutoI
        if minutoI > minutoF:
            hora -= 1
            minuto = (60 - minutoI) + minutoF
        if minutoI == minutoF:
            minuto = 0
    if horaI == horaF:
        if minutoI < minutoF:
            minuto = minutoF - minutoI
            hora = 0
        if minutoI > minutoF:
            minuto = (60 - minutoI) + minutoF
            hora = 23
        if minutoI == minutoF:
            hora = 24
            minuto = 0
        
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora, minuto))
    
def P1144():
    x = int(input())

    for i in range(1, x + 1):
        print(f'{i} {i ** 2} {i ** 3}')
        print(f'{i} {i ** 2 + 1} {i ** 3 + 1}')

def P1146():
    while True:
        x = int(input())
        
        if x == 0:
            break
        
        sequencia = ' '.join(map(str, range(1, x+1)))
        print(sequencia)
        