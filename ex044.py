print('-' * 12, 'Lojas Luan Magazine', '-' * 12)
compra = float(input('Qual o preço da compra? R$'))
print('''OPÇÕES DE PAGAMENTO
[ 1 ] À vista no dinheiro ou cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão com juros''')
opcao = int(input('Selecione uma das opção de pagamento: '))
if opcao == 1:
    valor = compra - (compra * 10 / 100)
    print('Sua compra com o desconto de 10% sai por R${:.2f}.'.format(valor))
elif opcao == 2:
    valor = compra - (compra * 5 / 100)
    print('Sua compra com o desconto de 5% sai por R${:.2f}.'.format(valor))
elif opcao == 3:
    valor = compra / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(valor))
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas deseja pagar? '))
    valor = compra + (compra * 20 / 100)
    valorParcela = valor / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f}, com juros de 20% \nA compra de R${:.2f} custará R${:.2f}.'.format(parcelas, valorParcela, compra, valor))