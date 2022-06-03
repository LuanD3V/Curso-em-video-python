maior = 0
menor = 0
for c in range (1, 6):
    p = float(input('Qual o peso da {} pessoa? '.format(c)))
    if p == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso lido foi de {:.1f}Kg \nO menor peso lido foi {:.1f}Kg'.format(maior, menor))