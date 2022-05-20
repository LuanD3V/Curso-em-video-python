d = int(input('Qual é a distância da viagem em km? '))
if d <= 200:
    print('A sua viagem de {}km, custará R${:.2f}.'.format(d, d * 0.50))
else:
    print('A sua viagem de {}km, custará R${:.2f}.'.format(d, d * 0.45))