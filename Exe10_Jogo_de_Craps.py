import random
import time

def JogaDados():
    lancamentos = random.randrange(2,13)
    return lancamentos

def Verificar_jogada(lance):
    if lance in [7,11]:
        print(f"Voce tirou {lance}, voce é natural")
    elif lance in [2,3,12]:
        print(f"Voce tirou {lance}, voce perdeu")
    else:
        print(f"Voce tirou {lance}, portanto,ganhou um ponto")
        tirado = lance
        lance2 = True
        while tirado != lance2:
            lance2 = random.randrange(2, 13)
            if lance2 == 7:
                print(f"Voce tirou {lance2},portanto, perdeu")
                break
            elif lance2 == tirado:
                print(f"Voce tirou {lance}, tirou o mesmo numero portanto, ganhou")
            else:
                print(f"Voce tirou {lance2}, jogue novamente em 3 segundos")
                time.sleep(3)

lance = JogaDados()
Verificar_jogada(lance)