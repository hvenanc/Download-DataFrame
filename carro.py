class Carro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor


c1 = Carro('Gol', 'Azul')
carros = [c1]

print([c1.nome for c1 in carros])