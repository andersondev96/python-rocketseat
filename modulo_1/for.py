print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("For utilizando dicionario - chaves")
for chave in pessoa.keys():
  print(chave)

print("\nFor utilizando dicionario - valores")
for valor in pessoa.values():
  print(valor)

print("\nFor utilizando dicionario - itens")
for chave, valor in pessoa.items():
 print(f"{chave}: {valor}") 

# range(): intervalo numérico
# [0,1,2,3,4]
print("\nUtilizando a função range()")
for numero in range(5):
  print("Numero:", numero)

print("\nUtilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
  if indice == 3:
    lista[indice] = 5
  else:
    lista[indice] = 0
print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f"{indice}: {valor}")
  if indice == 1:
    print("Indice 1")