from math import ceil
# Avaliação 1 - BSI


def duracao_partida(horas, minutos):
    """
    Elabore um programa que leia a duração de um partida em horas e minutos.
    Calcule e informe a duração total do partida em número de minutos.

    Exemplo:
    Número de horas: 2
    Número de minutos: 40
    Total de minutos: 160

    Argumentos:
        horas (int): uma quantidade de horas
        minutos (int): uma quantidade de minutos

    Retorna:
        (int): uma quantidade de minutos.
    """
    horasMinutos = horas * 60
    return horasMinutos + minutos


def jardas_para_metros(jardas):
    """
    1 jarda equivale a 0.9144 metros. Desenvolva uma função que receba um valor \
    em jardas e retorne o valor em metros.

    Argumentos:
        jardas (float): uma quantidade de jardas

    Retorna:
        (float): uma quantidade em metros, com 2 casas decimais.
    """
    metros = jardas * 0.9144
    return round(metros, 2)


def aluguel_booking(valor_diaria, dias):
    """
    Recebe uma quantidade de dias que ficou hospedado e o valor da
    diária, e retorna o valor a ser pago, considerando um acréscimo de
    R$ 85,00 para limpeza e 4% de taxa de administração sobre o valor
    do aluguel, sem a taxa de limpeza

    Argumentos:
        valor_diaria (float): o valor da diária
        dias (int): a quantidade de dias de hospedagem

    Retorna:
        float: o valor do aluguel, com duas casas decimais
    """
    valor = valor_diaria * dias
    taxaAdm = valor * 0.04
    return valor + taxaAdm + 85


def acesso_computadores(qt_alunos_total, qt_alunos_computador):
    """
    Você foi encarregado de realizar uma pesquisa sobre acesso a computadores.
    A sua pesquisa deverá apresentar o percentual de alunos da sua escola que possuem acesso computadores.
    Para isso, elabore um algoritmo que leia o número total de alunos da sua escola e o número de alunos que possuem acesso a computadores, por fim, com base nestes dados, escreva o percentual de alunos com acesso a computadores.
    Por exemplo, em uma escola com 500 alunos, apenas 200 alunos possuem acesso à Internet, o que equivale a 40% destes 500 alunos.

    Argumentos:
        qt_alunos_total (int): uma quantidade de horas
        qt_alunos_computador (int): uma quantidade de minutos

    Retorna:
        (float): percentual de alunos com acesso a computadores, com 2 casas decimais
    """
    percentual =  qt_alunos_computador * 100 / qt_alunos_total
    return round(percentual, 2)


def media_ponderada(prova, trabalho, exercicio):
    """
    Calcule a média ponderada, sabendo que os pesos são os seguintes:
    - prova: peso 5
    - trabalho: peso 3
    - exercício : peso 1

    Dica: eliminar os números mágicos.

    Argumentos:
        prova (float): nota de uma prova, entre 0 e 10.
        trabalho (float): nota do trabalho, entre 0 e 10.
        exercicio (float): nota do exercício, entre 0 e 10.

    Retorna:
        float: média ponderada das notas, com 1 casa decimal
    """
    media =  (prova * 5  + trabalho * 3  + exercicio * 1 ) / 9
    return round(media, 1)


def estacionamento(valor_30_minutos, qt_minutos_uso):
    """
    Elabore um programa para um estacionamento. O programa deve ler o valor para cada 30 minutos de uso do estacionamento e o tempo que o carro ficou estacionado em minutos. Informe o valor a ser pago pelo cliente, sabendo que as frações extras de 30 minutos devem ser cobradas de forma integral.

    Exemplo:
    Valor para 30 minutos RS: 5.00
    Minutos de uso: 70
    Total a Pagar R$: 15.00

    Argumentos:
        valor_30_minutos (float): o valor ser cobrado a cada 30 minutos
        qt_minutos_uso (int): a quantidade de minutos que foi utilizado

    Retorna:
        (float): o valor a ser pago, com 2 casas decimais
    """
    minutos = ceil(qt_minutos_uso / 30)
    valor = minutos * valor_30_minutos
    return valor



def trimestre(mes):
    """
    Dado um mês como um inteiro de 1 a 12, retorna a qual trimestre do ano ele \
        pertence como um número inteiro. 

    Por exemplo: mês 2 (fevereiro), faz parte do primeiro trimestre; \
    o mês 6 (junho), faz parte do segundo trimestre; \
    e o mês 11 (novembro), faz parte do quarto trimestre.

    Argumento
        mes (inteiro): o mês

    Returna:
        inteiro: o trimestre a que o mês pertence.
    """
    trimestres = {1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:4, 11:4, 12:4}
    return trimestres[mes]


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
    print("Duração da partida: ")
    test(duracao_partida(0, 0), 0)
    test(duracao_partida(1, 0), 60)
    test(duracao_partida(0, 1), 1)
    test(duracao_partida(1, 30), 90)
    test(duracao_partida(2, 40), 160)

    print("Metros para jardas: ")
    test(jardas_para_metros(1), 0.91)
    test(jardas_para_metros(2), 1.83)
    test(jardas_para_metros(3), 2.74)
    test(jardas_para_metros(4), 3.66)
    test(jardas_para_metros(5), 4.57)

    print("Aluguel do airBnB:")
    test(aluguel_booking(100, 1), 189.00)
    test(aluguel_booking(100, 2), 293.00)
    test(aluguel_booking(200, 10), 2165.00)
    test(aluguel_booking(50, 5), 345.00)

    print("Acesso Computadores:")
    test(acesso_computadores(500, 0), 0.00)
    test(acesso_computadores(500, 500), 100.00)
    test(acesso_computadores(500, 250), 50.00)
    test(acesso_computadores(500, 200), 40.00)
    test(acesso_computadores(495, 133), 26.87)

    print("Média ponderada:")
    test(media_ponderada(10, 10, 10), 10)
    test(media_ponderada(7, 7, 7), 7)
    test(media_ponderada(5, 8, 10), 6.6)
    test(media_ponderada(0, 0, 0), 0)

    print("Estacionamento: ")
    test(estacionamento(0, 0), 0)
    test(estacionamento(1, 0), 0)
    test(estacionamento(0, 1), 0)
    test(estacionamento(1, 1), 1)
    test(estacionamento(5, 70), 15)
    test(estacionamento(2, 7), 2)
    test(estacionamento(3, 25), 3)

    print("Trimestre: ")
    test(trimestre(1), 1)
    test(trimestre(2), 1)
    test(trimestre(3), 1)
    test(trimestre(4), 2)
    test(trimestre(5), 2)
    test(trimestre(6), 2)
    test(trimestre(7), 3)
    test(trimestre(8), 3)
    test(trimestre(9), 3)
    test(trimestre(10), 4)
    test(trimestre(11), 4)
    test(trimestre(12), 4)


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
