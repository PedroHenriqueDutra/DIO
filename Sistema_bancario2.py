class Cliente:

    def __init__:
        self.saldo=0
    

    def sacar(self,valor):
        if valor<=self.saldo:
            print("Valor sacado co sucesso: ")
            self.saldo-=valor
        else:
            print(f"O saldo não é o suficiente, o saldo atual é {self.saldo}")
    
    def deposito(self,valor):
        self.saldo+=valor
cliente= Cliente()
cliente.deposito(150)
        