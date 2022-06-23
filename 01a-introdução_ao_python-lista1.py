# Lista de exercícios 1 - variáveis e operadores

from math import ceil


def soma_dois_inteiros(a, b):
    """Recebe dois números inteiros, e retorna a sua soma.

    Argumentos:
        a (int): 1o valor;
        b (int): 2o valor;

    Retorna:
        int: a soma dos dois valores.
    """
    return a + b


def metro_para_milimetros(metros):
    """Recebe um valor em metros, e retorna o valor em milímetros,
        sabendo que 1 metro equivale a 1000 milimetros.

        Argumento:
        metros (float): um valor em metros;

    Retorna:
        float: o valor convertido para milimetros,
    """
    return metros * 1000


def tempo_para_percorrer_uma_distancia(distancia, velocidade):
    """Recebe uma distância e a velocidade de movimentação, e retorna
        as horas que seriam gastas para percorrer em linha reta.

    Argumentos:
        distancia (float): a distância, em kilômetros.
        velocidade (float): a velocidade, em kilômetros por hora.

    Retorna:
        float: o tempo, em horas.
    """
    tempo = round(distancia / velocidade, 2)
    return tempo


def aumento_salarial(salario, porcentagem):
    """Recebe um salário e sua porcentagem de aumento, e retorna
        o novo salário.

    Argumentos:
        salario (float): o salário original.
        porcentagem (float): o percentual de aumento, entre 0 e 100.

    Retorna:
        float: o novo salário, com duas casas decimais.
    """
    novoSalario = round(salario + (salario * (porcentagem/100)), 2)
    return novoSalario


def preco_com_desconto(preco_original, percentual_desconto):
    """Recebe um preço e sua porcentagem de desconto, e retorna
        o novo preço.

    Argumentos:
        preco_original (float): o preco original do produto.
        percentual_desconto (float): o percentual de desconto, entre 0 e 100.

    Returns:
        float: o preço final, após o desconto, com duas casas decimais.
    """
    precoDescontado = round(preco_original - (preco_original * (percentual_desconto/100)), 2)
    return precoDescontado


def dias_para_segundos(dias, horas, minutos, segundos):
    """Recebe uma data em dias com horas, minutos e segundos, e retorna
    a data em segundos.

    Argumentos:
        dias (int): a quantidade de dias.
        horas (int): a quantidade de horas.
        minutos (int): a quantidade de minutos.
        segundos (int): a quantidade de segundos.

    Retorna:
        int: a quantidade de segundos equivalente aos valores de dias, horas, minutos e segundos.
    """
    diasSegundos = dias * 24 * 60 * 60
    horasParaSegundos = horas * 60 * 60
    minutosParaSegundos = minutos * 60
    return segundos + diasSegundos + horasParaSegundos + minutosParaSegundos


def celsius_para_fahrenheit(celsius):
    """Recebe uma temperatura em graus Celsius, e retorna a temperatura
        em graus Fahrenheit.

    Argumento:
        celsius (float): a temperatura em graus Celsius.

    Retorna:
        float: a temperatura em graus Farenheit.
    """
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit


def fahrenheit_para_celsius(farenheit):
    """Recebe uma temperatura em graus Fahrenheit, e retorna a temperatura
        em graus Celsius.

    Argumento:
        farenheit (float): a temperatura em graus Fahrenheit.

    Retorna:
        float: a temperatura em graus Celsius.
    """
    celsius = round((farenheit - 32) / (9/5), 2)
    return celsius


def preco_aluguel_carro(dias, km):
    """Recebe uma quantidade de dias que o carro foi alugado e a
        quantidade de quilômetros rodados, e retorna o valor a ser pago.
        1 dia: 60 reais mais R$ 0,15 por km rodado.

    Argumentos:
        dias (int): quantidade de dias que o carro foi alugado.
        km (float): quantos quilômetros o carro rodou.

    Retorna:
        float: o preço do aluguel do carro, com 2 casas decimais,
                conforme a fórmula dada no enunciado.
    """
    valorPagar = dias * 60 + km * 0.15
    return valorPagar


def dias_perdidos_por_fumar(cigarros_fumados_por_dia, anos_fumando):
    """Recebe uma quantidade de cigarros fumados por dia e a quantidade
        de anos que fuma, e retorna o total de dias perdidos, sabendo que
        cada cigarro reduz a vida em 10 minutos.

    Argumentos:
        cigarros_fumados_por_dia (int): a quantidade de cigarros fumados por dia.
        anos_fumando (int): a quantidade de anos que a pessoa fumou.

    Retorna:
        int: a quantidade de dias que a pessoa perdeu por fumar.
    """
    diasPerdidos = int(cigarros_fumados_por_dia * anos_fumando * 365 * 10 / 60 / 24)
    return diasPerdidos


def dois_elevado_a_dez_mil():
    """Calcula dois elevado a dez mil, e retorna a quantidade de
    algarismos.

    Retorna:
        int: a quantidade de algarismos que o resultado contém.
    """
    algarismos = len(str(2**10000))
    return algarismos


def media_final_aprovado_reprovado(p1, p2, ep1, ep2):
    """Recebe as notas das 2 provas e 2 exercícios de programação e retorna
        se o aluno foi ou não aprovado. As provas têm peso 7 e os exercícios
        têm peso 3. Cada parcial tem peso igual.
        Uma forma de resolver é calcular a 1a parcial, com a média ponderada entre
        p1 e ep1, depois calcular a 2a parcial, com as notas de p2 e ep2 e depois
        calcular a média aritmética entre a 1a e a 2a parcial.

    Argumentos:
        p1 (float): a nota da primeira prova.
        p2 (float): a nota da segunda prova.
        ep1 (float): a nota do 1o exercício.
        ep2 (float): a nota do 2o exercício.

    Returns:
        bool: True ou False, dependendo da média ser maior ou igual a 7 ou não.
    """
    parcial1 = p1 * 0.7 + ep1 * 0.3 
    parcial2 = p2 * 0.7 + ep2 * 0.3
    media = (parcial1 + parcial2) / 2
    if media >= 7:
        return True
    else:
        return False


def salario(valor_hora, horas_mensais):
    """Recebe quanto ganha por hora e quantas horas trabalho ao mês,
    e retorna o salário líquido.

    Descontos:
    - INSS é 8% do salário bruto
    - IR é 11% do salário bruto
    - Sindicato é 5% do salário bruto.

    Argumentos:
        valor_hora (float): o valor hora pago ao funcionário.
        horas_mensais (float): a quantidade de horas trabalhadas no mes.

    Returns:
        float: o salário líquido, após todos os descontos.
    """
    salarioBruto = valor_hora * horas_mensais
    salarioLiquido = salarioBruto - salarioBruto * 0.24
    return salarioLiquido


def duzias(ovos):
    """Receba o número de ovos e devolva a quantidade de dúzias
        correspondente. Considere sempre dúzias cheias, arredondando pra
        cima se necessário.

    Argumento:
        ovos (int): a quantidade de ovos.

    Retorna:
        int: a quantidade de dúzias correspondente à quantidade de ovos,
            arredondado pra cima.
    """
    duzias = ceil(ovos / 12)
    return duzias


def tinta(metros_pintar):
    """Recebe quantos metros quadrados precisa pintar,
        e retorna a quantidade de latas de tinta a comprar.
        A cobertura da tinta é de 3 metros por litro de tinta.
        Cada lata possui 18 litros de tinta.

    Argumento:
        metros_pintar (float): a quantidade de metros quadrados a pintar.

    Retorna:
        int: a quantidade de latas de tinta, arredondado pra cima.
    """
    latas = ceil(metros_pintar / 3 / 18)
    return latas


def decompor_numero(n):
    """Leia um número inteiro menor que 1000 e devolva a quantidade de
        centenas, dezenas e unidades do mesmo.
        Obs.: não utilize operações com strings.

    Argumento:
        numero (int): um número menor que 1000.

    Retorna:
        tupla de inteiros, com as centenas, dezenas e unidades do numero.
    """
    centenas = int(n / 100)
    dezenas = int((n - (centenas * 100)) / 10)
    unidades = n - centenas * 100 - dezenas * 10
    tupla = (centenas, dezenas, unidades)
    return tupla


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
    print("Soma dois inteiros:")
    test(soma_dois_inteiros(0, 0), 0)
    test(soma_dois_inteiros(-1, 0), -1)
    test(soma_dois_inteiros(1, 1), 2)
    test(soma_dois_inteiros(0, -1), -1)
    test(soma_dois_inteiros(10, 10), 20)
    test(soma_dois_inteiros(-10, -10), -20)
    test(soma_dois_inteiros(-10, 20), 10)

    print("Metros para milimetros:")
    test(metro_para_milimetros(0), 0)
    test(metro_para_milimetros(1), 1000)
    test(metro_para_milimetros(1.8), 1800)
    test(metro_para_milimetros(1.81), 1810)

    print(
        "Tempo gasto para percorrer um distancia a uma velocidade"
        "constante(linha reta):"
    )
    test(tempo_para_percorrer_uma_distancia(1330, 20), 66.50)
    test(tempo_para_percorrer_uma_distancia(1000, 100), 10.00)
    test(tempo_para_percorrer_uma_distancia(1000, 123), 8.13)
    test(tempo_para_percorrer_uma_distancia(100000, 201), 497.51)

    print("Aumento salarial baseado na porcentagem de aumento:")
    test(aumento_salarial(1330, 20), 1596.00)
    test(aumento_salarial(1000, 0), 1000.00)
    test(aumento_salarial(1000.10, 123), 2230.22)
    test(aumento_salarial(0.0, 200), 0.00)

    print("Desconto do preco atual baseado na porcentagem do desconto:")
    test(preco_com_desconto(1330, 20), 1064.00)
    test(preco_com_desconto(1000, 0), 1000.00)
    test(preco_com_desconto(1000.10, 5.5), 945.09)
    test(preco_com_desconto(0.0, 200), 0.00)

    print("Dias,horas,minutos e segundos para segundos:")
    test(dias_para_segundos(0, 0, 0, 0), 0)
    test(dias_para_segundos(0, 0, 0, 1), 1)
    test(dias_para_segundos(0, 0, 0, 30), 30)
    test(dias_para_segundos(0, 0, 1, 0), 60)
    test(dias_para_segundos(0, 0, 1, 1), 61)
    test(dias_para_segundos(0, 1, 0, 0), 3600)
    test(dias_para_segundos(0, 0, 60, 0), 3600)
    test(dias_para_segundos(1, 0, 0, 0), 86400)
    test(dias_para_segundos(1, 1, 1, 1), 90061)
    test(dias_para_segundos(0, 23, 59, 59), 86399)
    test(dias_para_segundos(10, 20, 59, 1), 939541)

    print("Celsius para Fahrenheit:")
    test(celsius_para_fahrenheit(0), 32.00)
    test(celsius_para_fahrenheit(100), 212.00)
    test(celsius_para_fahrenheit(30), 86.00)
    test(celsius_para_fahrenheit(300), 572.00)
    test(celsius_para_fahrenheit(-100), -148.00)
    test(celsius_para_fahrenheit(1), 33.80)

    print("Fahrenheit para Celsius:")
    test(fahrenheit_para_celsius(32), 0)
    test(fahrenheit_para_celsius(212), 100)
    test(fahrenheit_para_celsius(30), -1.11)
    test(fahrenheit_para_celsius(300), 148.89)
    test(fahrenheit_para_celsius(-100), -73.33)
    test(fahrenheit_para_celsius(1), -17.22)

    print("Preco a pagar pelo aluguel do carro:")
    test(preco_aluguel_carro(10, 100), 615.00)
    test(preco_aluguel_carro(13, 133), 799.95)
    test(preco_aluguel_carro(1, 0), 60.00)
    test(preco_aluguel_carro(3, 79), 191.85)

    print("Total de dias que perdeu de viver por ter fumados:")
    test(dias_perdidos_por_fumar(10, 10), 253)
    test(dias_perdidos_por_fumar(13, 13), 428)
    test(dias_perdidos_por_fumar(0, 110), 0)
    test(dias_perdidos_por_fumar(3, 79), 600)

    print("Calcula a quantidade de algarismos que há em dois elevado a dez mil:")
    test(dois_elevado_a_dez_mil(), 3011)

    print("Média final:")
    test(media_final_aprovado_reprovado(10, 10, 0, 0), True)
    test(media_final_aprovado_reprovado(0, 0, 10, 10), False)
    test(media_final_aprovado_reprovado(10, 10, 10, 10), True)
    test(media_final_aprovado_reprovado(0, 0, 5, 0), False)
    test(media_final_aprovado_reprovado(8.0, 7.0, 9.0, 8.0), True)

    print("Salário líquido:")
    test(salario(10, 80), 608)
    test(salario(100, 30), 2280)
    test(salario(2.5, 300), 570)
    test(salario(5, 120), 456)

    print("Dúzias:")
    test(duzias(12), 1)
    test(duzias(24), 2)
    test(duzias(11), 1)
    test(duzias(23), 2)

    print("Latas de tinta:")
    test(tinta(10), 1)
    test(tinta(100), 2)
    test(tinta(560), 11)
    test(tinta(50001), 926)

    print("Decompor número:")
    test(decompor_numero(326), (3, 2, 6))
    test(decompor_numero(320), (3, 2, 0))
    test(decompor_numero(310), (3, 1, 0))
    test(decompor_numero(305), (3, 0, 5))
    test(decompor_numero(300), (3, 0, 0))
    test(decompor_numero(100), (1, 0, 0))
    test(decompor_numero(101), (1, 0, 1))
    test(decompor_numero(311), (3, 1, 1))
    test(decompor_numero(111), (1, 1, 1))
    test(decompor_numero(12), (0, 1, 2))
    test(decompor_numero(25), (0, 2, 5))
    test(decompor_numero(20), (0, 2, 0))
    test(decompor_numero(10), (0, 1, 0))
    test(decompor_numero(21), (0, 2, 1))
    test(decompor_numero(11), (0, 1, 1))
    test(decompor_numero(16), (0, 1, 6))
    test(decompor_numero(1), (0, 0, 1))
    test(decompor_numero(7), (0, 0, 7))


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
