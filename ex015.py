dias = (int(input('Quantos dias o carro foi alugado? ')))
km = float(input('Quantos Km foram rodados? '))
preco = (60.00 * dias) + (0.15 * km)
print('O total a pagar será R${:.2f}'.format(preco))