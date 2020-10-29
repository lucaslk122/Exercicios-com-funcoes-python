def QtsDigitos(n):
    txt = str(n)
    return len(txt)

n = int(input("Digite um numero: "))
print(f"O numero informado tem {QtsDigitos(n)} digitos")