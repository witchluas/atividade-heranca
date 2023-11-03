class Animal():

    def __init__(self,nome, cor):
        self.nome = nome
        self.cor = cor
    def emitir_som (self):
            print(f"O {self.nome} está fazendo barulho...")

    def comer (self):
        print(f"O {self.nome} foi comer...")

class Gato (Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som (self):
            print(f"O {self.nome} está miando...")

class Cachorro (Animal):
    def __int__(self, nome, cor):
        super(). __init__(nome, cor)

    def emitir_som(self):
        print(f"O {self.nome} está latindo...")

class Coelho (Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f"O {self.nome} está chiando...")

class Vaca (Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f"O {self.nome} está mugindo...")





