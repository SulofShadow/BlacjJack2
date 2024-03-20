from random import randint


class Baralho:
    def __init__(self):
        self.carta = []

    def __str__(self):
        return (f"""        ____________
        |{self.desenhar_numero()}         |
        |{self.desenhar_naipe()}         |
        |          |
        |    {self.desenhar_naipe()}     |
        |         {self.desenhar_naipe()}|
        |         {self.desenhar_numero()}|
        ------------
        """)

    def puxar_carta(self):
        self.carta = [randint(1, 13), randint(1, 4)]
        return self.carta

    def desenhar_naipe(self):
        naipe = {
            1: '♥',
            2: '♦',
            3: '♣',
            4: '♠'
        }
        return naipe[int(self.carta[1])]

    def desenhar_numero(self):
        desenhar_numero = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K',
        }
        if self.carta[0] in desenhar_numero:
            return desenhar_numero[int(self.carta[0])]
        else:
            return self.carta[0]


# IMPLEMENTAR TOTAL
carta_mesa1 = Baralho()
carta_mesa2 = Baralho()

carta_mesa1.puxar_carta()
carta_mesa2.puxar_carta()

print(carta_mesa1)
print(carta_mesa2)

# Implementar remove de duplicatas. Não pode existir 2 setes de paus
