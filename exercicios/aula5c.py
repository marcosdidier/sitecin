x = float(input('Digite o valor da coordenada x: '))
y = float(input('Digite o valor da coordenada y: '))

if x > 0 and y > 0: 
    print('Seu ponto está no quadrante 1')

elif y > 0:
    print('Seu ponto está no quadrante 2')

elif x > 0:
    print('Seu ponto está no quadrante 4')

else:
    print('Seu ponto está no quadrante 3')