n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Reprovado')
elif m >= 5.0 and m <= 6.9:
    print('Recuperação')
elif m >= 7.0:
    print('Aprovado, Parabéns')
else:
    print('Valores incorretos, tente novamente!')
print('Com a primeira nota sendo {:.1f}, e a segunda {:.1f}, sua média final é {:.1f}.'.format(n1, n2, m))