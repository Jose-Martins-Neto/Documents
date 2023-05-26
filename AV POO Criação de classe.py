class Pessoa:

    def __init__ (self,nome,peso,idade,comendo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo



    def comer(self, fruta):

        if self.comendo == False:

            self.fruta = fruta
            print(f'{self.nome} foi comer {self.fruta}')
            self.comendo = True

        else:
            print(f"{self.nome} nao pode comer pois Já está comendo")

    def stopcomer(self):
        if self.comendo == True:
            self.comendo = False
            print("Pare de comer")
        else:
            print("ele nao ta comendo")

p1 = Pessoa("Joao", 53,19)
p2 = Pessoa("Martins", 85,19)

p1.comer("laranja")
p1.stopcomer()