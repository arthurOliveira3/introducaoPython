import matplotlib.pyplot as plt

def f(x):
    return (
        -3.510*x**5 + 0.571*x**4 + 16.126*x**3 + -7.193*x**2 + 4.705*x + 0.912
    )

começo = -20.0
fim = 20.0
x = 0
intervaloPositivo = 100000000
intervaloNegativo = -100000000
x1 = 0
x2 = 0

while começo <= fim:
    x = começo
    funcao = f(x)
    if funcao < intervaloPositivo and funcao > 0:
        intervaloPositivo = funcao
        x1 = x
        print(f'{x} | {intervaloPositivo}')
    elif funcao > intervaloNegativo and funcao < 0:
        intervaloNegativo = funcao
        x2 = x
        print(f'{x} | {intervaloNegativo}')
    começo += 0.5

media = (x1 + x2) / 2
mediaAnterior = 0
convergencia = 10 #10**-6
iteracao = 0
listaErros = []
listaIteracoes = []

while abs(media - mediaAnterior) < convergencia and iteracao < 100:
    if f(media) > 0 and f(x1) > 0:
        x1 = media
    elif f(media) < 0 and f(x2) < 0:
        x2 = media
    listaErros.append(abs(media - mediaAnterior))
    listaIteracoes.append(iteracao)
    mediaAnterior = media
    media = (x1 + x2) / 2
    iteracao += 1
    print(f"\n{iteracao}: x1:{x1}  x2:{x2}  media:{media}  media Anterior:{mediaAnterior}")

print(f"\n\nMenor intervalo encontrado: {x1} à {x2}\n")

plt.plot(listaIteracoes, listaErros)
plt.title("Erros x Iterações")
plt.xlabel("Iterações")
plt.ylabel("Erros Médias")
plt.show()