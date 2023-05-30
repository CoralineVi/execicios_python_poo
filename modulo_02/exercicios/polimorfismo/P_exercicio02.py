"""
Implemente uma classe base Veiculo com atributos nome e limite de velocidade. Em seguida, crie classes derivadas como:
Carro, Moto e Caminhao, que herdam os atributos de Veiculo, então crie uma função acelerar() que recebe como argumento um objeto
e interage de maneira diferente em cada classe.
"""

class Veiculo:
    def __init__(self, modelo):
        self.modelo = modelo


class Carro(Veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)
        self.limite_velocidade = 75


class Moto(Veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)
        self.limite_velocidade = 100


class Caminhao(Veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)
        self.limite_velocidade = 50


def acelerar(veiculo):
    print(f"{veiculo.modelo} acelerando... {veiculo.limite_velocidade}Km/h velocidade máxima atingida!!")


# Objetos
carro_1 = Carro("Fiat")
moto_1 = Moto("Honda")
caminhao_1 = Caminhao("Ford")
#

# Testando função acelerar
acelerar(carro_1)
acelerar(moto_1)
acelerar(caminhao_1)
#
