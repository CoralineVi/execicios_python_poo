"""
Crie uma classe Cachorro com os atributos nome, idade e raca.
Instancie dois objetos dessa classe e exiba suas informações.
"""

class Cachorro:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        pass

cachorro1 = Cachorro("Rex", 3, "Golden Retriever")

print(cachorro1.idade)
