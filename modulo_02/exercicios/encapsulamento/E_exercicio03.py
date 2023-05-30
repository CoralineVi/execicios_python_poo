"""
Crie uma classe Produto com os atributos nome, preco e desconto. 
Utilize o encapsulamento para tornar o atributo desconto privado e crie um método para aplicar o desconto ao preço do produto.
"""

class Produto:
    def __init__(self, nome, preco, desconto):
        self.nome = nome
        self.preco = preco
        self.__desconto = desconto
        pass
    
    def getter_info(self):
        print(f"""Nome do produto: {self.nome}
Preço do produto: R${self.preco}""")
        pass
    
    def setter_desconto(self):
        self.preco -= self.__desconto
        print(f"Desconto de {self.__desconto} aplicado {self.nome}!!")
        pass
    
camisa = Produto("Camisa", 80, 20)

camisa.getter_info()
camisa.setter_desconto()
camisa.getter_info()
