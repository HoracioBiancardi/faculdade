class Imc:
    def __init__(self, peso, altura) -> None:
        self.peso = peso
        self.altura = altura

    def calculo(self):
        total = self.peso / (self.altura ** 2)
        return total
