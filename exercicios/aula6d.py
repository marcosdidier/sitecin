n = int(input())

while 0 > n or n > 100:
    print('Inválido!')
    n = int(input('Digite novamente: '))


if n % 2 == 0:
    n += 1

for i in range (n, 99, 2):
    print(i)

else:
    print(i + 2)