lista = [128391724, 23479479883, 3649826598769834, 418237695618937, 285792876579867845, 3758276986495872]
tamanho = len(lista)
meio = int(tamanho / 2)
lista1 = lista[:meio]
lista2 = lista[meio:]
lista_soma = []

for i in range(3):
    lista_soma.append(lista1[i] + lista2[i])

print(lista1)
print(lista2)
print(lista_soma)
