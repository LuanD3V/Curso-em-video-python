v = int(input('Qual é a velocidade atual do carro? '))
l = 80
if v <= l:
    print('Tenha um bom dia! Dirija com segurança.')
else:
    print('MULTADO! Você exedeu o limite de {}km/h \nVocê deve pagar uma multa de R${:.2f}'.format(l, (v - l) * 7))
print('---Fim---')