"""
Crie uma classe chamada Pessoa com os atributos nome e idade. Utilize o encapsulamento para torná-los privados. 
Em seguida, crie uma classe Aluno que herda de Pessoa e adiciona o atributo matricula. Implemente métodos para acessar e modificar a matrícula. 
Por fim, crie uma função que recebe uma lista de objetos Pessoa (que podem ser tanto objetos Pessoa quanto objetos Aluno) 
e exibe o nome e a idade de cada pessoa, usando o polimorfismo para tratar os objetos de forma genérica.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
    def getter_matricula(self):
        print(f"""Nome: {self._nome}
Idade: {self._idade}
Matrícula: {self.matricula}""")
    
    def setter_matricula(self):
        nova_matricula = str(input("""
(Somente números)
(4 digitos)
Digite o novo número de matrícula: """))
        try:
            int(nova_matricula)
        except ValueError:
            raise ValueError("Somente números são aceitos")
        if len(nova_matricula) == 4:
            self.matricula = nova_matricula
        else:
            print("Número inserido maior ou menor que 4 digitos")


def mostrar_pessoas(lista_pessoas):
    n = 1
    for pessoa in lista_pessoas:
        print(f"""
============
  Pessoa {n}
============
Nome: {pessoa._nome}
Idade: {pessoa._idade}""")
        if isinstance(pessoa, Aluno):
            print(f"Matrícula: {pessoa.matricula}")
        n += 1


aluno1 = Aluno("Jhin", 44, 4444)
pessoa1 = Pessoa("Vivi", 66)
lista_pessoas = [aluno1, pessoa1]

aluno1.setter_matricula()

mostrar_pessoas(lista_pessoas)
