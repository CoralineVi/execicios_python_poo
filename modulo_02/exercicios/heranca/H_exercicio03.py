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
        return area
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return perimetro


class Triangulo(Forma):
    def __init__(self, base, altura, lado1, lado2, lado3):
        super().__init__(base, altura)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area
    
    def calcular_perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro


# Objetos
retangulo_1 = Retangulo(5, 5)
triangulo_1 = Triangulo(5, 5, 3, 3, 3)
#

# Retangulo
print(retangulo_1.calcular_area())
print(retangulo_1.calcular_perimetro())
#

# Triangulo
print(triangulo_1.calcular_area())
print(triangulo_1.calcular_perimetro())
#
