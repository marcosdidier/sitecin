peso = float(input('Digite o seu peso em quilogramas: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso/altura ** 2

if imc > 30:
    print('Você está obeso.')

elif imc > 25:
    print('Você está acima do peso.')

elif imc > 18.5: 
    print('Você está com o peso normal')

else:
    print('Você está abaixo do peso.')