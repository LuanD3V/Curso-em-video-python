from time import sleep
from random import randint
print('=-' * 12, 'JOKENPO GAME', '=-' * 12)
itens = ('Pedra', 'Papel', 'Tesoura')
player = int(input(''' Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Escolha: '''))
cpu = randint(0, 2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('=-' *15)
print('O Computador escolheu {} \nO jogador escolheu {}'.format(itens[cpu], itens[player]))
print('=-' *15)
if cpu == 0:
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('JOGADOR GANHOU')
    elif player == 2:
        print('COMPUTADOR GANHOU')
elif cpu == 1:
    if player == 0:
        print('COMPUTADOR GANHOU')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('JOGADOR GANHOU')
elif cpu == 2:
    if player == 0:
        print('JOGADOR GANHOU')
    elif player == 1:
        print('COMPUTADOR GANHOU')
    elif player == 2:
        print('EMPATE')
else:
    print('Jogada inválida')