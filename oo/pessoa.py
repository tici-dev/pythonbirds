class Pessoa:
    def __init__(self, *filhos, nome:None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"

if __name__ == '__main__':
    bia = Pessoa(nome='bia')
    tici = Pessoa(bia, nome= 'tici')
    print(id(tici))
    print(tici.cumprimentar())
    print(tici.nome)
    print(tici.idade)
    for filho in tici.filhos:
        print(filho.nome)
    tici.sobrenome = 'moreira'
    del tici.filhos
    print(tici.__dict__)
    print(tici.__dict__)
