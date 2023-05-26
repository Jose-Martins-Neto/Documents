class Conta:

    def __init__(self, numero_conta, tipo_conta, nome_cliente):
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        self.saldo = 0
        self.status=False
        self.nome_cliente = nome_cliente

    def deposito(self, valor):

        if valor >= 0:
            if self.status==True:
                self.saldo += valor
            print(
                f"O valor depositado foi de R$ {valor}, seu saldo atual é de R$ {self.saldo} e a sua conta está ativa.")
        else:
            print(f"A sua conta não possui nenhum valor depositado, ela está inativa.")
            self.status=False

    def saque(self, valor_saque):

        if valor_saque >= 0:
            self.status==False
            self.saldo -= valor_saque
            print(f"O valor sacado foi de R$ {valor_saque}, seu saldo atual é de R$ {self.saldo}.")
        else:
            print(f"O valor sacado não pode ser igual ou menor que zero!")

    def verifica_saldo(self):
        print(f"O seu saldo é de R${self.saldo}")

    def ativar_conta(self):
        if self.status!=True:
            print("Sua conta foi ativada com sucesso.")
            self.status=True
        else:
            print(f"A sua conta ja estava ativada.")
            self.status=True

    def desativar_conta(self):
        if self.status==True:
            print("Sua conta foi desativada com sucesso.")
            self.status=False
        else:
            print(f"A sua conta ja está desativada.")
            self.status=False


    def informaçao_conta(self):
        print(f"Olá {self.nome_cliente}, sua conta é do tipo {self.tipo_conta} com a numeração {self.numero_conta}")


conta1=Conta(25547, "conta corrente", "rayane")
conta1.deposito(450.23)
conta1.saque(200.00)
conta1.verifica_saldo()
conta1.informaçao_conta()