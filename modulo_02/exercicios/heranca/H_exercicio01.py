"""
Crie uma classe base chamada Animal com o método fazer_som(). 
Em seguida, crie duas classes derivadas, como Cachorro e Gato, que herdam de Animal
e implementam o método fazer_som() com sons diferentes para cada classe.
"""

class Animal:
    def __init__(self, nome):
        self.nome = nome


class Cachorro(Animal):
    def fazer_som(self):
        print(f"O cachorro {self.nome} latiu")

class Gato(Animal):
    def fazer_som(self):
        print(f"O gato {self.nome} miou")

gato_1 = Gato("Nya")
cachorro_1 = Cachorro("Rex")

gato_1.fazer_som()
cachorro_1.fazer_som()
