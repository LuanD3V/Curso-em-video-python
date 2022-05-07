sal = float(input('Qual é o salário do funcionário? R$'))
a = (sal * 15) /100
print('O funcionário que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}.'.format(sal, sal + a))