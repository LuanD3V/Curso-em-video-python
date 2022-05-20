s = float(input('Qual o salário do funcionário? R$'))
if s <= 1250.00:
    ns = (s * 15) / 100 + s
    print('O salário que era R${:.2f}, com o acréscimo de 15%, será de R${:.2f}'.format(s, ns))
else:
    ns = (s * 10) / 100 + s
    print('O salário que era R${:.2f}, com o acréscimo de 10%, será de R${:.2f}'.format(s, ns))