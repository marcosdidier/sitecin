numero_celebridades = int(input())
celebridade = 'a'
ye = 'a'
zagueirao = 'a'
chris = 'a'
candidatos = 'a'
tay = 'a'
katy = 'a'
ariana = 'a'
bey = 'a'
shakira = 'a'
ranktay = 0
rankkaty = 0
rankariana = 0
rankbey = 0
rankshak = 0


for i in range(numero_celebridades):
    celebridade = input()
    print(f'Apresentador: Contamos com a ilustre presença de {celebridade}, uma salva de palmas!')
    #Processo abaixo feito para armazenar esses valores nas strings caso essas celebridades apareçam e o código poder compará-las mais na frente
    if celebridade == 'Kanye West':
        ye = 'Kanye West'
    if celebridade == 'Gerard Piqué':
        zagueirao = 'Gerard Piqué'
    if celebridade == 'Chris Martin':
        chris = 'Chris Martin'

while candidatos != 'Início da Premiação':
    candidatos = input()
    if candidatos == 'Taylor Swift':
        tay = 'TAYLOR SWIFT'
        ranktay = 5
    if candidatos == 'Katy Perry':
        katy = 'KATY PERRY'
        rankkaty = 4
    if candidatos == 'Ariana Grande':
        ariana = 'ARIANA GRANDE'
        rankariana = 3
    if candidatos == 'Beyoncé':
        bey = 'BEYONCÉ'
        rankbey = 2
    if candidatos == 'Shakira':
        shakira = 'SHAKIRA'
        rankshak = 1

print('Apresentador: Vamos deixar de enrolação e ir para a premiação!')
print('Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...')

if ranktay == 5:
    print(tay)
    if ye == 'Kanye West':
        print('Kanye West: Eu vou te deixar terminar. Estou feliz por você, mas Beyoncé fez um dos melhores vídeos de todos os tempos.')

elif ranktay == 0 and rankkaty == 4:
    print(katy)

elif ranktay == 0 and rankkaty == 0 and rankariana == 3:
    print(ariana)

elif ranktay == 0 and rankkaty == 0 and rankariana == 0 and rankbey == 2:
    print(bey)
    if chris == 'Chris Martin':
        print('Chris Martin: Minha heroína, minha irmã, meu tudo. Você merece!')

elif ranktay == 0 and rankkaty == 0 and rankariana == 0 and rankbey == 0 and rankshak == 1:
    print(shakira)
    if zagueirao == 'Gerard Piqué':
        print('Gerard Piqué: Meu amor me perdoa, volta pra mim...')


