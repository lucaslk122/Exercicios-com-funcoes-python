"""
Exercicio 96 "Curso em video" 
def Area(largura,comprimento):
    area = largura*comprimento
    
    print(f"A area  do terreno é {area}m^2")

largura = int(input("Digite a largura do terreno: "))
comprimento = int(input("Digite a largura do terreno: "))
Area(largura,comprimento)
"""

"""
Exercicio 97 "Curso em video" 
def Escreva(texto):
    print("~"*len(texto))
    print(texto)
    print("~"*len(texto))


texto = input("Entre com a mensagem: ")
Escreva(texto)
"""

"""
Exercicio 98 "Curso em video" 
Faça um prorgrama que tenha uma função chamada contador(), que receba tres parametros; inicio, fim, e passo e realize a contagem.
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
def Contador(inicio,fim,passo):
    for i in range(1,11):
        print(i,end=" ")
    print("="*30)
    for i in range(10,-1,-2):
        print(i,end=" ")
    print("="*30)
    if passo != 0:
        for i in range(inicio,fim+1,passo):
            print(i,end=" ")
        print("="*30)
        else:
            for i in range(inicio,fim,1):
                print(i,end=" ")
        print("="*30)

inicio = int(input("Digite o inicio da contagem: "))
fim = int(input("Digite o fim da contagem: "))
passo = int(input("Digite o passo da contagem: "))
Contador(inicio,fim,passo)
#"""


"""
import random
from time import sleep

def Sorteia(lista):
    print("Sorteando 5 valores da lista: ",end="")
    for i in range(0,5):
        n = random.randint(1,10)
        lista.append(n)
        print(f"{n}", end=" ", flush=True)
        sleep(0.3)
    print("Pronto!")

def SomaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f"Somando os valores pares de {lista}, temos {soma}")

numero = list()
Sorteia(numero)  
SomaPar(numero)
"""

"""
#Aprendendo a fazer docstring
def Contador(inicio,fim,passo):
    for i in range(inicio,fim,passo):
        print(i , end=" ")

Contador(1,10,1)
"""
"""
#Colocando parametros opcionais
def Somar(a,b,c=0):
    s = a + b + c
    print(f"Soma = {s}")

#a = int(input("Digite valor de a: "))
#b = int(input("Digite valor de b: "))
#c = int(input("Digite valor de c: "))
Somar(1,2,8)
"""
"""
#returnando valores de uma função
def Somar(a=0,b=0,c=0):
    s = a + b + c
    return s #aqui, ele ira pegar o valor calculado de s, e irá retornar esse valor para a função Somar

a = int(input("Digite valor de a: "))
b = int(input("Digite valor de b: "))
c = int(input("Digite valor de c: "))
print(Somar(a,b,c))
"""

#Fatorial com função que retorna um valor
def Fatorial(n):
    f = 1
    for c in range(n,0,-1):
        f *= c
    return f

n = int(input("Digite um numero: "))
print(f"O fatorial de {n} é {Fatorial(n)}")

