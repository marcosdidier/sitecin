local = str(input())
hora = int(input())
resposta = str(input())

if local == 'Salão' :
    print('Em direção ao salão!')
    print(f'Pra chegar na hora, vou ter que sair de {hora - 2} horas.')

elif local == 'Praça':
    print('Para a praça eu vou!')
    print(f'Pra chegar na hora, vou ter que sair de {hora - 2} horas.')

elif local == 'Centro da cidade' :
    print('Faz tempo que não visito o centro, mal posso esperar!')
    print(f'Pra chegar na hora, vou ter que sair de {hora - 1} horas.') 

if resposta == 'Sim, Pearl! Siga seus sonhos!':
    print('Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!')

elif resposta == 'Não. Você ficará na fazenda.':
    print('Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!')