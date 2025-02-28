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