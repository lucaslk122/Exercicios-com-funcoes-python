def valorPagamento(valor_prestação,dias_atraso):
    if dias_atraso == 0:
        return "O valor a ser pago é o da propria prestação"
    else:
        pagar = valor_prestação + (valor_prestação*0.03) + (valor_prestação*dias_atraso*0.001)
        return f"O valor a ser pago é R${pagar}"


while True:
    valor_prestação = float(input("Digite o valor da prestação  R$: "))
    dias_atraso = int(input("Digite os dias em atraso: "))
    resp = valorPagamento(valor_prestação,dias_atraso)
    print(resp)
    if valor_prestação != 0:
        continue
    else:
        break
