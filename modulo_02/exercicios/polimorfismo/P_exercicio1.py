"""
Crie uma função chamada som_animal que recebe um objeto Animal como parâmetro e chama o método fazer_som(). 
Chame essa função com objetos de diferentes classes derivadas e observe o comportamento polimórfico.
"""

class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca


class Gato(Animal):
    def __init__(self, nome, raca, som):
        super().__init__(nome, raca)
        self.som = som


class Cachorro(Animal):
    def __init__(self, nome, raca, som):
        super().__init__(nome, raca)
        self.som = som

def fazer_som(animal):
    print(f"O {animal.raca} faz {animal.som}")


# Objetos
cachorro_1 = Cachorro("Aysha", "Chowchow", "AuAu!")
gato_1 = Gato("Zael", "Persa", "Miau")
#

fazer_som(cachorro_1)
fazer_som(gato_1)
