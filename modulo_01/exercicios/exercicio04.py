"""
Crie uma classe ContaBancaria com os atributos numero e saldo. 
Implemente métodos depositar e sacar para adicionar e retirar dinheiro da conta.
"""

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        pass
    
    def depositar(self, valor):
        self.saldo += valor
        return (f"O valor {valor} foi depositado com sucesso")
    
    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            return (f"O valor {valor} foi retirado com sucesso")
        else:
            return (f"O valor de R${valor} não pode ser retirado: Saldo insuficiente")

conta1 = ContaBancaria(1000)

print(f"Saldo atual: {conta1.saldo}")
print(conta1.sacar(300))
print(f"Saldo atual: {conta1.saldo}")
print(conta1.depositar(600))
print(f"Saldo atual: {conta1.saldo}")
print(conta1.sacar(1400))
print(f"Saldo atual: {conta1.saldo}")
