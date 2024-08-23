def criar_pessoa(nome,idade):
    pessoa = {}
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    return pessoa

lista_pessoas = [{'nome':'Douglas','idade':16},
                 {'nome':'Christian','idade':16}
                 ]
tamanho_lista = len(lista_pessoas)
index = 0

while(tamanho_lista > 0):
    pessoa = criar_pessoa(lista_pessoas[index]['nome'], lista_pessoas[index]['idade'])
    print(pessoa)
    tamanho_lista = tamanho_lista - 1
    index = index + 1