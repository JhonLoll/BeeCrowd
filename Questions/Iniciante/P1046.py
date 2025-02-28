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