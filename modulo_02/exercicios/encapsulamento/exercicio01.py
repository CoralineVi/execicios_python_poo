"""
Crie uma classe chamada Pessoa com os atributos nome e idade. Utilize o encapsulamento para
definir esses atributos como privados e crie métodos para acessá-los (getters) e modificá-los (setters).
"""
import time

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        pass
    
    def getter_infos(self):
        print(f"Nome: {self.__nome} | Idade: {self.__idade}")
        pass
    
    def setter_nome(self):
        self.__nome = str(input("Novo nome: "))
        pass
    
    def setter_idade(self):
        self.__idade = int(input("Nova idade: "))
        pass
    

pessoa1 = Pessoa("Vinícius", 17)

pessoa1.setter_idade()
pessoa1.getter_infos()
pessoa1.setter_nome()
pessoa1.getter_infos()