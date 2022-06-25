# Avaliação 2 - BSI


def soma_dobro(num1, num2):
    """
    Dados dois números inteiros retorna sua soma,
    porém se os números forem iguais retorna o dobro da soma.
    """
    soma = num1 + num2
    if num1 == num2:
        return soma * 2
    else:
        return soma


def soma_dez(num1, num2):
    """
    Dados dois inteiros, retorna True se um dos dois é 10 ou a soma é 10.
    """
    return num1 == 10 or num2 == 10 or num1 + num2 == 10


def troca_primeira_e_ultima(texto):
    """
    Seja uma string,
    se ela tiver tamanho <= 1 retorna ela mesma,
    caso contrário troca a primeira e a última letra.
    """
    if len(texto) <= 1:
        return texto
    else:
        return texto[-1] + texto[1:-1] + texto[0]


def nove_na_frente(lista):
    """
    Verifica se pelo menos um dos quatro primeiros itens é nove.
    """
    return 9 in lista[:4]


def metade_inicial(texto):
    """
    Seja uma string, retorna a primeira metade da string.
    """
    metade = int(len(texto) / 2)
    return texto[:metade]


def pontas_removidas(texto):
    """
    Seja uma string de pelo menos dois caracteres,
    retorna uma string sem o primeiro e último caracter.
    """
    return texto[1:-1]


def dois_giros_a_esquerda(texto):
    """
    Rodar à esquerda uma string em duas posições.
    A string possui pelo menos 2 caracteres.
    """
    return texto[2:] + texto[:2]


def igual_inicio_fim(lista):
    """
    Retorna True se a lista possui pelo menos um elemento
    e o primeiro elemento é igual ao último
    """
    return len(lista) >= 1 and lista[0] == lista[-1]


def inverte_numero(numero):
    """
    Receba um inteiro positivo e o mostre invertido.
    Ex.: 1234 gera 4321
    """
    return int(str(numero)[::-1])


def pontas_do_nome(nome):
    """Dada uma string contendo o nome completo de uma pessoa,
    retorne uma nova string contendo o primeiro e o último nome, em
    maiúsculas.
    "Marco André Lopes Mendes" -> "MARCO MENDES"
    """
    lista = nome.split(" ")
    primeiroNome = lista[0].upper()
    sobrenome = lista[-1].upper()
    return primeiroNome + " " + sobrenome


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
    print("soma_dobro")
    test(soma_dobro(1, 2), 3)
    test(soma_dobro(3, 2), 5)
    test(soma_dobro(2, 2), 8)
    test(soma_dobro(-1, 0), -1)
    test(soma_dobro(0, 0), 0)
    test(soma_dobro(0, 1), 1)

    print("dez")
    test(soma_dez(9, 10), True)
    test(soma_dez(9, 9), False)
    test(soma_dez(1, 9), True)
    test(soma_dez(10, 1), True)
    test(soma_dez(10, 10), True)
    test(soma_dez(8, 2), True)
    test(soma_dez(8, 3), False)
    test(soma_dez(10, 42), True)
    test(soma_dez(12, -2), True)

    print("troca")
    test(troca_primeira_e_ultima("code"), "eodc")
    test(troca_primeira_e_ultima("a"), "a")
    test(troca_primeira_e_ultima("ab"), "ba")
    test(troca_primeira_e_ultima("abc"), "cba")
    test(troca_primeira_e_ultima(""), "")
    test(troca_primeira_e_ultima("Chocolate"), "ehocolatC")
    test(troca_primeira_e_ultima("nythoP"), "Python")
    test(troca_primeira_e_ultima("hello"), "oellh")

    print("nove_na_frente")
    test(nove_na_frente([1, 2, 9, 3, 4]), True)
    test(nove_na_frente([1, 2, 3, 4, 9]), False)
    test(nove_na_frente([1, 2, 3, 4, 5]), False)
    test(nove_na_frente([9, 2, 3]), True)
    test(nove_na_frente([1, 9, 9]), True)
    test(nove_na_frente([1, 2, 3]), False)
    test(nove_na_frente([1, 9]), True)
    test(nove_na_frente([5, 5]), False)
    test(nove_na_frente([2]), False)
    test(nove_na_frente([9]), True)
    test(nove_na_frente([]), False)
    test(nove_na_frente([3, 9, 2, 3, 3]), True)

    print("primeira_metade")
    test(metade_inicial("papagaio"), "papa")
    test(metade_inicial("Lula"), "Lu")
    test(metade_inicial("abcdef"), "abc")
    test(metade_inicial("ab"), "a")
    test(metade_inicial(""), "")
    test(metade_inicial("0123456789"), "01234")
    test(metade_inicial("buraco"), "bur")
    test(metade_inicial("joinville"), "join")

    print("sem_pontas")
    test(pontas_removidas("Beleza"), "elez")
    test(pontas_removidas("Python"), "ytho")
    test(pontas_removidas("codigo"), "odig")
    test(pontas_removidas("sala"), "al")
    test(pontas_removidas("ab"), "")
    test(pontas_removidas("Chocolate!"), "hocolate")
    test(pontas_removidas("cozinha"), "ozinh")
    test(pontas_removidas("Uhull"), "hul")

    print("gira_esquerda_2")
    test(dois_giros_a_esquerda("Beleza"), "lezaBe")
    test(dois_giros_a_esquerda("python"), "thonpy")
    test(dois_giros_a_esquerda("Oi"), "Oi")
    test(dois_giros_a_esquerda("code"), "deco")
    test(dois_giros_a_esquerda("tio"), "oti")
    test(dois_giros_a_esquerda("12345"), "34512")
    test(dois_giros_a_esquerda("Chocolate"), "ocolateCh")
    test(dois_giros_a_esquerda("tijolo"), "joloti")

    print("inicio_fim_igual")
    test(igual_inicio_fim([1, 2, 3]), False)
    test(igual_inicio_fim([1, 2, 3, 1]), True)
    test(igual_inicio_fim([1, 2, 1]), True)
    test(igual_inicio_fim([7]), True)
    test(igual_inicio_fim([]), False)
    test(igual_inicio_fim([7, 7]), True)

    print("número invertido")
    test(inverte_numero(1), 1)
    test(inverte_numero(0), 0)
    test(inverte_numero(10), 1)
    test(inverte_numero(1111), 1111)
    test(inverte_numero(00000), 0)
    test(inverte_numero(1234), 4321)
    test(inverte_numero(2013), 3102)
    test(inverte_numero(20130711), 11703102)

    print("nomes_pontas")
    test(pontas_do_nome("Ivo Riegel"), "IVO RIEGEL")
    test(pontas_do_nome("Eduardo da Silva"), "EDUARDO SILVA")
    test(pontas_do_nome("Fernando José Braz"), "FERNANDO BRAZ")
    test(pontas_do_nome("Marco André Lopes Mendes"), "MARCO MENDES")
    test(pontas_do_nome("Paulo César de Oliveira"), "PAULO OLIVEIRA")


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
