"""
Crie uma classe Carro com os atributos marca, modelo e ano. 
Implemente um método descricao que retorna uma string com as informações do carro.
"""

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        pass
    
    def descricao(self):
        return (
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Ano: {self.ano}"
        )

carro_1 = Carro("Fiat", "Fusca", 1982)

print(carro_1.descricao())