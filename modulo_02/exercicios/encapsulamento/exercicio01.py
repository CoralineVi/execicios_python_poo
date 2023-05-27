"""
Crie uma classe chamada Pessoa com os atributos nome e idade. Utilize o encapsulamento para
definir esses atributos como privados e crie métodos para acessá-los (getters) e modificá-los (setters).
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        pass
    
    def getter_infos(self):
        print(f"")
