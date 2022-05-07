p = float(input('Qual é o preço do produto? R$'))
d = (5 * p) / 100
print('O produto que custava R${:.2f}, na promoção de 5% vai custar R${:.2f}.'.format(p, p - d))
