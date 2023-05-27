"""
Implemente uma hierarquia de classes para um sistema de funcionários de uma empresa. 
Crie uma classe base Funcionario com atributos como nome e salario, e em seguida crie classes derivadas como:
Gerente, Analista e Estagiario, cada uma com atributos específicos e comportamentos adicionais.
"""

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario
        pass
    
    def getter_infos(self):
        print(f"Nome: {self.nome} | Salário: {self._salario}")
        pass
    
    def getter_infos_funcionario(self, funcionario):
        if self.nv_hierarquia >= 2:
            print(f"Nome: {funcionario.nome} | Salário: {funcionario._salario}")
        else:
            print("Permissão negada")
        pass
    

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.nv_hierarquia = 3
    
    def setter_salario(self, funcionario, valor):
        if self.nv_hierarquia > funcionario.nv_hierarquia:
            funcionario._salario = valor
            print(f"Salário do {funcionario.nome} atualizado | Novo salário: R${valor}")
        else:
            print("Permissão negada")
        pass
    

class Analista(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.nv_hierarquia = 2
    

class Estagiario(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.nv_hierarquia = 1
    
    def trabalhar(self):
        print(f"Pois é amigo {self.nome}, a vida de estágiario é difícil")
        pass
    

o_gerente1 = Gerente("Gerente Carlos", 3000)
o_gerente2 = Gerente("Gerente Igor", 3100)
o_analista = Analista("Analista Vitor", 2000)
o_estagiario = Estagiario("Estagiario Luan", 1000)

# Testes com o gerente1
o_gerente1.getter_infos()
o_gerente1.getter_infos_funcionario(o_analista)
o_gerente1.setter_salario(o_analista, 1500)
o_gerente1.getter_infos_funcionario(o_analista)

o_gerente1.setter_salario(o_gerente2, 2500) # Testando funcionamento do nível hierarquico
o_gerente1.getter_infos_funcionario(o_gerente2)
#

# Testes com analista
o_analista.getter_infos()
o_analista.getter_infos_funcionario(o_gerente1)
o_analista.getter_infos_funcionario(o_estagiario)
#

# Estagiario trabalhando, nada fora do comum aqui
o_estagiario.trabalhar()
#