cond1 = False
cond2 = False
dicionario_tempo = {}
lista_escolas = []
lista_quesitos = []
dicionario_notas = {}

while not cond1:
    nome = input()
    if nome == 'Não há mais escolas':
        cond1 = True
    tema_desfile, tempo_desfile = input(), int(input())
    dicionario_tempo.update({nome : tempo_desfile})

while not cond2:
    quesito = input()
    if quesito == 'Não há mais quesitos':
        cond2 = True
    escolas_e_notas = input()