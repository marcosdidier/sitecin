nome = str(input('Digite o seu nome: '))

#Cálculo calorias gastas
print(f'Olá, {nome}! Seja bem vindo')
taxa_basal = float(input('Digite a sua taxa metabólica basal: '))
exercicio_fisico = float(input('Digite a quantidade de calorias diárias gastas fazendo exercícios físicos: '))
frequencia_exercicio = int(input('Digite a quantidade de vezes que você faz exercício na semana: '))
descanso = int(input('Digite a quantidade de meses que você descansa por ano: '))
calorias_gastas = float(taxa_basal * 7 * 4 * 12 + exercicio_fisico * frequencia_exercicio * (12-descanso) * 4 / 12)

#Impressão calorias gastas
print(f'Rui, você gasta {calorias_gastas:.2f} calorias por ano!')

#Cálculo calorias adquiridas
calorias_refeicao = float(input('Digite a quantidade de calorias que você ingere por refeição: '))
refeicoes_dia = int(input('Digite a quantidade de vezes que você come por dia: '))
calorias_ingeridas_ano = calorias_refeicao * refeicoes_dia * 7 * 4 * 12

#Impressão calorias adquiridas
print(f'{nome}, realizamos o cálculo! \nVocê consome {calorias_ingeridas_ano:.2f} calorias por ano. \nO seu saldo calórico anual é de {calorias_ingeridas_ano-calorias_gastas :.2f}')

#Cálculo final
if calorias_ingeridas_ano >= calorias_gastas : 
    print('Infelizmente você não irá perder peso caso continue com essa rotina!')
else :
    print('Parabéns, você está no caminho certo!')