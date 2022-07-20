# Avaliação 3 - BSI
# Utilize for ou while em todo os problemas abaixo.



def limpa_texto(texto):
    """
    Faça uma função que receba um texto e retorne apenas as letras.
    Remova números, espaços e caracteres de pontuação.

    Argumento:
        texto (string): um texto contendo letras, números, sinais de pontuação e espaços em branco.

    Retorna:
        string: uma string contendo apenas as letras.
    """
    letras = ['a','b','c','ç','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','á','à','â','ã','é','ê','ẽ','í','î','ĩ','ó','ô','õ','ú','û','ũ']
    novoTexto = ''
    for i in texto:
        if i.lower() in letras:
            novoTexto += i
    return novoTexto


def camel_casing(s):
    """
    Camel Casing é uma forma de escrever nomes de identificadores, (como varíaveis e funções) usando letras maiúsculas para separar as palavras.
    A palavra "camel" em inglês significa camelo (lembre-se das córcovas do camelo e tudo faz sentido). Desenvolva uma solução que quebre o "camel casing", usando espaços entre as palavras.

    Exemplo
    "camelCasing"  =>  "camel Casing"
    "mediaFinalAposRecuperacao"  =>  "media Final Apos Recuperacao"
    "soma"   =>  "soma"
    "" =>  ""

    Argumento:
        s (string): a palavra original que será processada.

    Returna:
        string: um conjunto de palavras, que foram separadas segundo o critério do "camel casing".
    """
    novoTexto = ''
    for i in s:
        if i == i.upper():
            novoTexto += f' {i}'
        else:
            novoTexto += i
    return novoTexto


def divisiveis_por_sete_unicos_ordenados(numeros):
    """
    Faça uma função que receba uma lista e retorne uma nova lista,
    com os números divisíveis por 7, em ordem crescente, sem repetição.

    Argumento:
        numeros: uma lista de números.

    Retorna:
        list: uma lista, de acordo com o critério estabelecido.
    """
    novaLista = []
    for i in numeros:
        if i % 7 == 0 and i not in novaLista:
            novaLista.append(i)
    return sorted(novaLista)


def crescimento_populacional_2(populacao_atual, percentual, aumento, populacao_final):
    """
    Determine quantos anos a população da cidade levará para ultrapassar a população final. Os valores de população atual, percentual de aumento anual, aumento por mudança e da população final são informados como parâmetros da função.

    Aqui vai um exemplo: suponha que a população é p0 = 1000 no início do ano. A população aumenta regularmente em 2% ao ano e, além disso, 50 novos habitantes por ano vêm morar na cidade.

    Quantos anos a cidade precisa para ver sua população maior ou igual a p = 1200 habitantes?

    No final do primeiro ano, haverá:
    1000 + 1000 * 0,02 + 50 => 1070 habitantes (o número de habitantes é um inteiro)

    No final do 2º ano, haverá:
    1070 + 1070 * 0,02 + 50 => 1141 habitantes

    No final do 3º ano, haverá:
    1141 + 1141 * 0,02 + 50 => 1213

    Serão necessários 3 anos inteiros.

    Observação:
    Não se esqueça de converter o parâmetro de porcentagem em porcentagem no corpo de sua função: se o parâmetro de porcentagem for 2, você deve convertê-lo para 0,02.

    Argumentos:
        populacao_atual (int): a população inicial, no ano zero.
        percentual (float): o percentual de aumento da população a cada ano.
        aumento (int): a quantidade de pessoas que chegam na cidade de fora.
        populacao_final (int): a população que se quer chegar.

    Returna:
        int: a quantidade de anos até se alcançar (ou passar) a população final.
    """
    anos = 0
    while populacao_atual < populacao_final:
        populacao_atual += populacao_atual * (percentual / 100) + aumento
        anos += 1
    return anos


def fibonacci2(n):
    """
    Retorne uma lista com os elementos até chegar no valor de n.
    Fibonacci = 1,1,2,3,5,8,13,...

    Argumento:
        n (int): o valor limite do termo da série.

    Retorna:
        uma lista de elementos inteiros.
    """
    listaFibonacci = [1]
    ultimo = listaFibonacci[-1]
    penultimo = 0
    while ultimo < n:
        listaFibonacci.append(ultimo + penultimo)
        penultimo = ultimo
        ultimo = listaFibonacci[-1]
    return listaFibonacci



# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = f"\033[31m{'Falhou'}"
    else:
        prefixo = f"\033[32m{'Passou'}"
        acertos += 1
    print(f"{prefixo} Esperado: {esperado} \tObtido: {obtido}\033[1;m")


def main():

    print("Limpa texto:")
    test(limpa_texto("BSI1 Programação 1"), "BSIProgramação")
    test(limpa_texto("BSI1-Programação1!"), "BSIProgramação")
    test(limpa_texto("(47) 9 9988-7766"), "")

    print("Camel Casing:")
    test(camel_casing("helloWorld"), "hello World")
    test(camel_casing("camelCase"), "camel Case")
    test(camel_casing("breakCamelCase"), "break Camel Case")
    test(
        camel_casing("quantidadeDeDiasPerdidosPorFumar"),
        "quantidade De Dias Perdidos Por Fumar",
    )
    test(camel_casing("mediaFinalAposRecuperacao"), "media Final Apos Recuperacao")

    print("Divisíveis por sete únicos ordenados:")
    test(divisiveis_por_sete_unicos_ordenados([2, 2]), [])
    test(divisiveis_por_sete_unicos_ordenados([1, 6, 14]), [14])
    test(divisiveis_por_sete_unicos_ordenados([1, 7, 14]), [7, 14])
    test(divisiveis_por_sete_unicos_ordenados([14, 1, 2, 7]), [7, 14])
    test(divisiveis_por_sete_unicos_ordenados([21, 1, 7, 23, 7, 14, 7, 5]), [7, 14, 21])

    print("Crescimento Populacional 2:")
    test(crescimento_populacional_2(1000, 2, 50, 1200), 3)
    test(crescimento_populacional_2(1500, 5, 100, 5000), 15)
    test(crescimento_populacional_2(1500000, 2.5, 10000, 2000000), 10)

    print("Fibonnaci 2:")
    test(fibonacci2(3), [1, 1, 2, 3])
    test(fibonacci2(5), [1, 1, 2, 3, 5])
    test(fibonacci2(7), [1, 1, 2, 3, 5, 8])
    test(fibonacci2(20), [1, 1, 2, 3, 5, 8, 13, 21])


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
