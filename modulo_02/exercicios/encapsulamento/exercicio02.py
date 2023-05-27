"""
Implemente uma classe ContaBancaria com os atributos saldo e limite. 
Utilize o encapsulamentopara tornar esses atributos privados e forneça métodos para depositar e sacar dinheiro da conta, 
respeitando o limite.
"""

class ContaBancaria:
    def __init__(self, saldo, limite):
        self.__saldo = saldo
        self.__limite = limite
        pass
    
    def setter_saque(self, valor):
        if valor < self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso")
        else:
            print("Valor indisponível para o saque, verifique o seu saldo bancário")
    
    def setter_deposito(self, valor):
        if (self.__saldo + valor < self.__limite):
            self.__saldo += valor
            print(f"Deposito de R${valor} realizado com sucesso")
        else:
            print("Limite da conta atingido!!")
        return
    
    def getter_info(self):
        print(f"Saldo: {self.__saldo} | Limite: {self.__limite}")
        pass
    

conta1 = ContaBancaria(1000, 2000)

conta1.getter_info()
conta1.setter_deposito(1000)
conta1.getter_info()
