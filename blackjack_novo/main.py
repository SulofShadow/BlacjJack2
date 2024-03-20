from random import randint

dinheiro_total = float(input(f'Quantidade na banca:R$').strip())
quatidade_rodada = float(input(f'Quantidade na rodada:R$').strip())

#fazer isso de um jeito que fique só uma, provavelmente com poo. o primeiro valor é o numero e o segundo é o naipe
cartas_mesa1 = [randint(1, 13), randint(1, 4)]
cartas_mesa2 = [randint(1, 13), randint(1, 4)]

#desenho do naipe
desenhar_naipe = {
    1: '♥',
    2: '♦',
    3: '♣',
    4: '♠'
}
#desenho do numero. Essas partes terão que ir para o print das cartas depois
desenhar_numero = {
    1: 'A',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'J',
    12: 'Q',
    13: 'K',
}

total_cartas = cartas_mesa1[0] + cartas_mesa2[0]

#gambiarra para fazer os jkq ficarem 10
if cartas_mesa2[0] == 11:
    total_cartas -= 1
elif cartas_mesa2[0] == 12:
    total_cartas -= 2
elif cartas_mesa2[0] == 13:
    total_cartas -= 3

if cartas_mesa1[0] == 11:
    total_cartas -= 1
elif cartas_mesa1[0] == 12:
    total_cartas -= 2
elif cartas_mesa1[0] == 13:
    total_cartas -= 3


#megagambiarra para o As
if cartas_mesa1[0] == 1:
    if total_cartas <= 10:
        total_cartas += 10

if cartas_mesa2[0] == 1:
    if total_cartas <= 10:
        total_cartas += 10


#desenho das cartas
print(f"""____________
|{desenhar_numero[int(cartas_mesa1[0])]}         |
|{desenhar_naipe[int(cartas_mesa1[1])]}         |
|          |
|          |
|         {desenhar_naipe[int(cartas_mesa1[1])]}|
|         {desenhar_numero[int(cartas_mesa1[0])]}|
------------
""")
print(f"""____________
|{desenhar_numero[int(cartas_mesa2[0])]}         |
|{desenhar_naipe[int(cartas_mesa2[1])]}         |
|          |
|          |
|         {desenhar_naipe[int(cartas_mesa2[1])]}|
|         {desenhar_numero[int(cartas_mesa2[0])]}|
------------
""")
print(f'total:{total_cartas}')