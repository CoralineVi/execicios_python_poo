"""
Crie uma classe Retangulo com os atributos largura e altura.
Implemente um método calcular_area que retorna a área do retângulo.
"""

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        pass
    
    def calcular_area(self):
        area = self.largura * self.altura
        return(area)

retangulo1 = Retangulo(5, 5)

print(retangulo1.calcular_area())
