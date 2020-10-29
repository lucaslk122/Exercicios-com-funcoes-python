def valorPagamento(valor_prestação,dias_atraso):
    if dias_atraso == 0:
        return "Sem atrasos, o valor a ser pago é o da propria prestação, ou seja, R$",valor_prestação
    else:
        return valor_prestação + (valor_prestação*0.03) + (valor_prestação*dias_atraso*0.001)


while True:
    valor_prestação = float(input("Digite o valor da prestação  R$: "))
    dias_atraso = int(input("Digite os dias em atraso: "))
    resp = valorPagamento(valor_prestação,dias_atraso)
    print(f"Valor a ser pago R${resp}")
    if valor_prestação != 0:
        continue
    else:
        break
