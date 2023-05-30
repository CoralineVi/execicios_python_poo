"""
Crie uma função chamada calcular_area_total que recebe uma lista de objetos Forma (da atividade de herança) 
e calcula a área total somando as áreas de cada forma. Chame essa função com diferentes objetos e verifique o comportamento polimórfico.
"""

# Tive problemas para importar de outra pasta, apesar da ideia ser praticar a modularização
# Para evitar que eu passasse mais tempo (passei 4 horas nessa atividade, decidi passar diretamente o código para cá)
# Estou pedindo ajuda em grupos de estudos, quanto eu conseguir faço a correção
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

#

def calcular_area_total(lista_formas):
    soma = 0
    for forma in lista_formas:
        if isinstance(forma, Forma):
            soma += forma.calcular_area()
        else:
            raise TypeError("A função calcular_area_total só recebe formas geométricas")
    print(f"A soma entre as áreas da lista de formas geométricas foi: {soma}")


retangulo_1 = Retangulo(5, 5)
retangulo_2 = Retangulo(5, 5)
triangulo_1 = Triangulo(5, 5, 5, 5, 5)
triangulo_2 = Triangulo(5, 5, 5, 5, 5)

lista_formas = [retangulo_1, retangulo_2, triangulo_1, triangulo_2]

calcular_area_total(lista_formas)
