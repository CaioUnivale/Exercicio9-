class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        taxa = 2
        if self.saldo + taxa >= valor:
            self.saldo -= valor + taxa
            return True
        else:
            return False

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return True
        else:
            return False


conta_bancaria = ContaBancaria("João", 1000)
print("Saldo inicial da ContaBancaria:", conta_bancaria.saldo)
conta_bancaria.depositar(500)
print("Saldo após depósito:", conta_bancaria.saldo)
conta_bancaria.sacar(300)
print("Saldo após saque:", conta_bancaria.saldo)

conta_poupanca = ContaPoupanca("Maria", 1500)
print("Saldo inicial da ContaPoupanca:", conta_poupanca.saldo)
conta_poupanca.sacar(200)
print("Saldo após saque da ContaPoupanca:", conta_poupanca.saldo)

conta_corrente = ContaCorrente("Pedro", 2000, 1000)
print("Saldo inicial da ContaCorrente:", conta_corrente.saldo)
conta_corrente.sacar(2500)
print("Saldo após saque da ContaCorrente:", conta_corrente.saldo)