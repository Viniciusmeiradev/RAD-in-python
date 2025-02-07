import os 

#Abrindo o arquivo
arquivo =  open('dados.txt', 'w', encoding = 'utf-8')

#Atributos
print("Nome do arquivo: ", arquivo.name)
print("Modo de abertura: ", arquivo.mode)
print("Arquivo fechado: ", arquivo.closed)

#Adiciona ao arquivo
arquivo.write("Pegue seu café porque novas noticias estão no há.")

#fechar o arquivo
arquivo.close()

#verificar se o arquivo estar aberto ou fechado
print('O arquivo estar aberto: ', arquivo.closed)

#Exibindo caminhos relativo e absoluto
relativo = os.path.relpath("dados.txt")
absoluto = os.path.abspath("dados.txt")
print("Caminho relativo: ", relativo)
print("Caminho absoluto ", absoluto)

#Abrindo o conteúdo
arquivo = open('dados.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
print("Tipo de conteúdo: ", type(conteudo))
print("Conteúdo do arquivo: ", repr(conteudo))
arquivo.close()