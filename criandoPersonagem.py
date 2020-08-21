# código de treino de classes
# o objetivo é criar uma classe de personagem de rpg, os parâmetros serão variados
# ok, começando...

class Personagem:
    def __init__(self):
        self.apelido = ''
        self.classe = ''
        self.funcao = ''
        self.armadura = ''
        self.arma = ''
        self.dificuldade = ''

    def atributos(self):
        print(''' Aqui está a ficha do seu personagem:
                  Nome: {} 
                  Classe: {}
                  Função: {}
                  Armadura: {}
                  Arma: {}
                  Dificuldade: {}'''.format(self.apelido, self.classe, self.funcao, self.armadura, self.arma,
                                            self.dificuldade))

    def criacao(self):
        self.apelido = str(input('qual é o nome do seu personagem? '))
        self.classe = str(input('qual é sua classe? '))
        self.funcao = str(input('qual é sua função no grupo? '))
        self.armadura = str(input('qual é a armadura que você usa? '))
        self.arma = str(input('qual é a arma que você usa? '))
        self.dificuldade = str(input('qual é a dificuldade do personagem? '))

ryan = Personagem()

