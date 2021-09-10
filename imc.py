class Imc:
    def __init__(self, peso, altura) -> None:
        self.peso = peso
        self.altura = altura

    def calculo(self) -> float:
        return self.peso / (self.altura ** 2)


horacio = Imc(97, 1.75)
print(horacio.calculo())