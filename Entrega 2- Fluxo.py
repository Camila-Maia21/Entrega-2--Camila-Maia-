import random


class Lutadores:
    def __init__ (self, nomelut, idade, peso, forca, faixa, artelut):
        self.nomelut = nomelut
        self.idade = idade
        self.peso = peso
        self.forca = forca
        self.faixa = faixa
        self.artelut = artelut
    def __str__ (self):
        return f'Lutadores nome: {self.nomelut} idade: {self.idade} peso: {self.peso} forca: {self.forca} faixa: {self.faixa} arte marcial: {self.artelut}'
    
class Torneios:
    def __init__ (self, nometor, artetor, faixas, pesos):
        self.nometor = nometor
        self.artetor = artetor
        self.faixas = faixas
        self.pesos = pesos
    def __str__ (self):
        return f'Torneios nome: {self.nometor} arte marcial: {self.artetor} faixas: {self.faixas} pesos: {self.pesos}'

Dicionario_Lutador = {}
Dicionario_Torneio = {}

        
print ('Escolha uma das opções abaixo:')
print ('1- Menu de torneio')
print ('2- Menu de lutador')
print ('3- Criar torneio aleatório')
numeroMenu = input ('Escreva o numero da opção desejada aqui: ')

if numeroMenu == '1':
    print ('Escolha uma das opções abaixo')
    print ('a- Criar torneio')
    print ('b- Inscrever lutador')
    print ('c- Ver torneios existentes')
    print ('d- Ver ranking de torneio')
    print ('e- Ver lutadores inscritos em torneio')
    print ('f- Realizar a luta')
    letraTorneio = input ('Escreva a letra da opção desejada aqui: ')

    if letraTorneio == 'a':
        nomeTorneio = input     ('Escreva o nome do torneio: ')
        arteMarcialtor = input  ('Escreva o nome da arte marcial: ')
        corFaixator = input     ('Escreva a cor da faixa do torneio: ')
        pesoTorneioi = input    ('Escreva o limite mínimo de peso: ')
        pesoTorneiof = input    ('Escreva o limite máximo de peso: ')
        print ('Torneio criado') 
        print (nomeTorneio)
        print (arteMarcialtor)
        print (corFaixator)
        print (pesoTorneioi)
        print (pesoTorneiof)
        Dicionario_Torneio = {nomeTorneio: 'Nome', arteMarcialtor: 'Arte marcial', corFaixator: 'Faixa', pesoTorneioi: 'Peso_mínimo', pesoTorneiof: 'Peso_máximo'}


    elif letraTorneio == 'b':
        nomeLutador = input  ('Escreva o nome do lutador: ')
        idadeLutador = input ('Escreva a idade do lutador: ')
        pesoLutador = input  ('Escreva o peso do lutador: ')
        forcaLutador = input ('Escreva a forca do lutador: ')
        faixaLutador = input ('Escreva a faixa do lutador: ')
        arteLutador = input  ('Escreva a arte marcial do lutador: ')
        print ('Lutador inscrito')
        Dicionario_Lutador = {nomeLutador : 'Nome', idadeLutador : 'Idade', pesoLutador: 'Peso', forcaLutador: 'Força', faixaLutador: 'Faixa', arteLutador: 'Arte marcial'}
        


    elif letraTorneio == 'c':
        m = Torneios('Torneio Judo A', 'Judo', 'Preta', 70)
        n = Torneios('Torneio MuayThai A', 'MuayThai', 'Azul', 90)
        u = Torneios('Torneio JiuJitsu A', 'JiuJitsu', 'Roxa', 90)
        o = Torneios('Torneio Judo B', 'Judo', 'Vermelha', 60)
        print (Dicionario_Torneio)
        print (m)
        print (n)
        print (u)
        print (o)


    elif letraTorneio == 'e':
        x = Lutadores('Roberto', 20, 75, 100, 'Preta', 'Judo')
        l = Lutadores('Anderson', 25, 70, 120, 'Preta', 'Judo')
        p = Lutadores('Alan', 27, 95, 130, 'Azul', 'MuayThai')
        y = Lutadores('Gustavo', 22, 90, 110, 'Azul', 'MuayThai')
        z = Lutadores('Marcio', 19, 100, 150, 'Roxa', 'JiuJitsu')
        w = Lutadores('Leonardo', 23, 95, 145, 'Roxa', 'JiuJitsu')
        k = Lutadores('Marcelo', 18, 65, 100, 'Vermelha', 'Judo')
        j = Lutadores('Antonio', 20, 60, 90, 'Vermelha', 'Judo')
        print (Dicionario_Lutador)
        print (x)
        print (l)
        print (p)
        print (y)
        print (z)
        print (w)
        print (k)
        print (j)
        
    
elif numeroMenu == '2':
    print ('Escolha uma das opções abaixo')
    print ('a- Cadastrar lutador')
    print ('b- Ver lutadores')
    print ('c- Ver detalhes de lutador')
    letraLutador = input ('Escreva a letra da opção desejada aqui: ')

    if letraLutador == 'a':
        nomeLutador = input  ('Escreva o nome do lutador: ')
        idadeLutador = input ('Escreva a idade do lutador: ')
        pesoLutador = input  ('Escreva o peso do lutador: ')
        forcaLutador = input ('Escreva a forca do lutador: ')
        faixaLutador = input ('Escreva a faixa do lutador: ')
        arteLutador = input  ('Escreva a arte marcial do lutador: ')
        print ('Lutador cadastrado')
        

    elif letraLutador == 'b':
        x = Lutadores('Roberto', 20, 75, 100, 'Preta', 'Judo')
        l = Lutadores('Anderson', 25, 70, 120, 'Preta', 'Judo')
        p = Lutadores('Alan', 27, 95, 130, 'Azul', 'MuayThai')
        y = Lutadores('Gustavo', 22, 90, 110, 'Azul', 'MuayThai')
        z = Lutadores('Marcio', 19, 100, 150, 'Roxa', 'JiuJitsu')
        w = Lutadores('Leonardo', 23, 95, 145, 'Roxa', 'JiuJitsu')
        k = Lutadores('Marcelo', 18, 65, 100, 'Vermelha', 'Judo')
        j = Lutadores('Antonio', 20, 60, 90, 'Vermelha', 'Judo')
        print (Dicionario_Lutador)
        print (x.nomelut)
        print (l.nomelut)
        print (p.nomelut)
        print (y.nomelut)
        print (z.nomelut)
        print (w.nomelut)
        print (k.nomelut)
        print (j.nomelut)

    elif letraLutador == 'c':
        x = Lutadores('Roberto', 20, 75, 100, 'Preta', 'Judo')
        l = Lutadores('Anderson', 25, 70, 120, 'Preta', 'Judo')
        p = Lutadores('Alan', 27, 95, 130, 'Azul', 'MuayThai')
        y = Lutadores('Gustavo', 22, 90, 110, 'Azul', 'MuayThai')
        z = Lutadores('Marcio', 19, 100, 150, 'Roxa', 'JiuJitsu')
        w = Lutadores('Leonardo', 23, 95, 145, 'Roxa', 'JiuJitsu')
        k = Lutadores('Marcelo', 18, 65, 100, 'Vermelha', 'Judo')
        j = Lutadores('Antonio', 20, 60, 90, 'Vermelha', 'Judo')
        print (Dicionario_Lutador)
        print (x)
        print (l)
        print (p)
        print (y)
        print (z)
        print (w)
        print (k)
        print (j)

    

    
    

    
    





    

