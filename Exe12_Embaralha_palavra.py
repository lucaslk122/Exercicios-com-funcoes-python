import random

def EmbaralhaPalavra(txt):
    txt = list(txt)
    random.shuffle(txt)
    return "".join(txt)

txt = input("Digite uma palavra: ").lower()
print((f"A palavra {txt} embaralhada ficou {EmbaralhaPalavra(txt)}"))