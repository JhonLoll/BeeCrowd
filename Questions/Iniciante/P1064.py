#? QUESTÕES RESOLVIDAS
# P1046() P1051() P1052() P1059() P1060() P1064() P1065() P1067() P1070()
# P1071() P1072() P1073() P1074() P1075() P1078() P1079() P1080() P1094()
# P1095() P1096() P1097() P1098() P1099() P1101() P1113() P1114() P1115()
# P1115() P1116() P1118() P1131() P1132() P1134() P1143()
#! QUESTÃO INCOMPLETA
#! P1051()

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