#Você devem cria seguinte variável, que é uma lista de dicionários:

lista_de_dicionarios = [{"nome":"andres","inicial":"AN","final":"ES"}
                       ,{"nome":"levi","inicial":"LE","final":"VI"}
                       ,{"nome":"nicolas","inicial":"NI","final":"AS"}
                       ,{"nome":"robson","inicial":"RO","final":"ON"}
                       ,{"nome":"thiago","inicial":"TH","final":"GO"}
                       ,{"nome":"giovany","inicial":"gi","final":"ny"}]

#Crie uma lista somente com os nomes dos dicionários usando "list comprehension" e print o type da lista e o retorno deve ser "list"

lista_nomes = [dicionario["nome"] for dicionario in lista_de_dicionarios]
print(lista_nomes)
print(type(lista_nomes))

#Crie um dicionário que deve conter nome, inicial, final usando "dict comprehension" e print: 

dicionario = {dicionario["nome"]:dicionario for dicionario in lista_de_dicionarios}
print(dicionario)
print(type(dicionario))

#A. Somente as chaves dos dicionários;

dicionario = {dicionario["nome"]:dicionario for dicionario in lista_de_dicionarios}
print(dicionario.keys())
print(type(dicionario.keys()))

#B. O nome com inicial;

dicionario = {dicionario["nome"]:dicionario["inicial"] for dicionario in lista_de_dicionarios}
print(dicionario)
print(type(dicionario))

#C. O nome com final

dicionario = {dicionario["nome"]:dicionario["final"] for dicionario in lista_de_dicionarios}
print(dicionario)
print(type(dicionario))
