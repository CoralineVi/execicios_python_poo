"""
Crie uma classe Aluno com os atributos nome e notas (uma lista de notas). 
Implemente um método calcular_media que calcula a média das notas do aluno.
"""

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        try:
            self.notas = list(notas)
        except:
            print("ERRO: Apenas listas são aceitas nas notas")
            exit()
        pass
    
    def calcular_media(self):
        soma_notas = 0
        for nota in self.notas:
            soma_notas += nota
        media = soma_notas / len(self.notas)
        return media

aluno1 = Aluno("Daniel", [8, 7, 6])

print(aluno1.calcular_media())
