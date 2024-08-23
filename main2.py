lista_pessoas = [{'nome':'Danilo','idade':101},
                 {'nome':'Joel','idade':54}
                 ]
class Pessoa:
    def __init__(self):
        ...
    def set_nome(self, nome):
        self.nome = nome
    def set_idade(self, idade):
        self.idade = idade
tamanho_lista = len(lista_pessoas)
index = 0
while(tamanho_lista > 0):
    pessoa = Pessoa()
    pessoa.set_nome(lista_pessoas[index]['nome'])
    pessoa.set_idade(lista_pessoas[index]['idade'])
    print(pessoa.nome)
    print(pessoa.idade)
    tamanho_lista = tamanho_lista - 1
    index = index + 1