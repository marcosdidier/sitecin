n = int(input('Digite um número de 0 a 100: ')) 
cond = False

while 0 > n or n > 100:
    print('Inválido!')
    n = int(input('Digite novamente: '))


while not cond:
    if n == 99 or n == 100:
        cond = True
    elif n % 2 == 0:
        print(f'{n + 1}, ' , end = '')
        n += 2
    elif n % 2 == 1:
        print(f'{n + 2}, ' , end = '')
        n += 2
        if n > 99:
            end = ''    
else:
    end = ''