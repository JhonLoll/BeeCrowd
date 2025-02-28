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