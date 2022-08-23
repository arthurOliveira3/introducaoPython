import random

def embaralhaPalavras(palavra):
    lista = list(palavra)
    random.shuffle(lista)
    palavraEmbaralhada = ''.join(lista)
    return palavraEmbaralhada

palavra = "chatonilda"
embaralhada = embaralhaPalavras(palavra)

for item in range(5):
    print(f"\nVocê tem {5 - item} tentativas")
    print(f"\nA palavra é:\n{embaralhada}")
    tentativa = input("\nDigite a palavra que você acha certa: ")
    tentativa = tentativa.lower()
    if len(tentativa) == len(palavra) and tentativa == palavra:

        print("PARABÉNS!!!")
        break

print(f"A palavra certa é:{palavra}")