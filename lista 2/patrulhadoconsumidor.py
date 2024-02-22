numero_compradores = int(input())
nome = 'a'
cpf = 'a'
nomeid = 'a'
cpfid = 'a'
qtd_ingressos = 0
preco_ingressos = 0
codigo_compra = 'a'
contador_criterios = 0
numeros_impares = 0
suspeitos = 0

for i in range (numero_compradores):
    nome = 'a'
    cpf = 'a'
    nomeid = 'a'
    cpfid = 'a'
    qtd_ingressos = 0
    preco_ingressos = 0
    codigo_compra = 'a'
    numeros_impares = 0
    contador_criterios = 0
    nome = input()
    cpf = input()
    nomeid = input()
    cpfid = input()
    qtd_ingressos = int(input())
    preco_ingressos = int(input())
    codigo_compra = input()
    
    if nome != nomeid:
        contador_criterios += 1
    
    if cpf != cpfid:
        contador_criterios += 1
    
    if qtd_ingressos > 12:
        contador_criterios += 1
    
    if preco_ingressos > 1500:
        contador_criterios += 1
    
    for x in codigo_compra:
        if x in '13579':
            numeros_impares += 1
    if numeros_impares >= 7:
        contador_criterios += 1
        
        
    if contador_criterios >= 3:
        suspeitos += 1

print(f'Total de compradores analisados: {numero_compradores}')
print(f'Total de suspeitas de cambistas: {suspeitos}')

    
