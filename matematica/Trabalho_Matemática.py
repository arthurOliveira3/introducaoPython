import matplotlib.pyplot as plt

funcao = 0
começo = -20.0
fim = 20.0
x = 0
intervaloPositivo = 100000000
intervaloNegativo = -100000000

while começo < fim:
    x = começo
    funcao = -3.510*x**5 + 0.571*x**4 + 16.126*x**3 + -7.193*x**2 + 4.705*x + 0.912
    if funcao > 0 and funcao < intervaloPositivo:
        intervaloPositivo = funcao
        print(f'{x} | {intervaloPositivo}')
    elif funcao > intervaloNegativo and funcao < 0:
        intervaloNegativo = funcao
        print(f'{x} | {intervaloNegativo}')
    começo += 0.5


media = intervaloPositivo + intervaloNegativo / 2
mediaAnterior = 0
listaErros = []
listaIteracoes = []
convergencia = 1000
iteracao = 0

while abs(media - mediaAnterior) < convergencia and iteracao <=10:
    if media > 0:
        intervaloPositivo = media
    elif media < 0:
        intervaloNegativo = media
    listaErros.append(media - mediaAnterior)
    listaIteracoes.append(iteracao)
    mediaAnterior = media
    media = intervaloPositivo + intervaloNegativo / 2
    iteracao += 1
    print("\n", media, mediaAnterior, iteracao)


print(  f'\nMenor Intervalo Positivo encontrado:',intervaloPositivo,
        f'\nMaior Intervalo Negativo encontrado:',intervaloNegativo,
        "\n")

plt.plot(listaIteracoes, listaErros)
plt.title("Erros x Medias")
plt.xlabel("Iterações")
plt.ylabel("Erros Medias")
plt.show()