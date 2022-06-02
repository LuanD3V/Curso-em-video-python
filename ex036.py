valorCasa = float(input('Qual O valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
financiamento = int(input('Quantos anos de financiamento? ')) * 12
parcela = valorCasa / financiamento
if parcela <= (salario * 30) / 100:
    print('Emprestimo ACEITO')
else:
    print('Emprestimo Negado')
print('Para pagar uma casa de R${:.2f}, em {} meses, a parcela será de R${:.2f}.'.format(valorCasa, financiamento, parcela))
