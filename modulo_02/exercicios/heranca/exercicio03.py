"""
Crie uma classe base "Forma". 
Em seguida, crie classes derivadas como Retangulo e Triangulo que herdam de "Forma" e 
implementam seus próprios cálculos de área e perímetro.
"""

class Forma:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    
    def calcular_area(self):
        area = self.base * self.altura
        print(f"Área do Retangulo = Base x Altura = {area}")
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        print(f"Perimetro do Retangulo = 2 * (Base + Altura) = {perimetro}")


class Triangulo(Forma):
    def __init__(self, base, altura, lado1, lado2, lado3):
        super().__init__(base, altura)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        area = (self.base * self.altura) / 2
        print(f"Área do Triângulo = (Base * Altura) / 2 = {area}")
    
    def calcular_perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        print(f"Perimetro do Triângulo = Lado 1 + Lado 2 + Lado 3 = {perimetro}")


# Objetos
retangulo_1 = Retangulo(5, 5)
triangulo_1 = Triangulo(5, 5, 3, 3, 3)
#

# Retangulo
retangulo_1.calcular_area()
retangulo_1.calcular_perimetro()
#

# Triangulo
triangulo_1.calcular_area()
triangulo_1.calcular_perimetro()
#
