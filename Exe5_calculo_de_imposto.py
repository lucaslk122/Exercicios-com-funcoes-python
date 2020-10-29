def SomaImposto(taxaImposto,custo):
    taxaImposto = taxaImposto/100
    ValorFinal = custo + (custo*taxaImposto)
    print(F"Valor final do produto: R${ValorFinal}")


taxaImposto = float(input("Digite a taxa de imposto: "))
custo = float(input("Digite o custo do produto: "))
SomaImposto(taxaImposto,custo)