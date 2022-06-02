from random import randint
from time import sleep
print('=-' * 12, 'JO KEN PO GAME', '=-' * 12)
p = int(input(''' Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Escolha: '''))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
c = randint(0, 2)
if c == p:
    print('EMPATE')
    if c == 0:
        c = 'Pedra'
        p = 'Pedra'
    elif c == 1:
        c = 'Papel'
        p = 'Papel'
    else:
        c = 'Tesoura'
        p = 'Tesoura'
elif c == 0 and p == 2:
    c = 'Pedra'
    p = 'Tesoura'
    print('COMPUTADOR GANHOU')
elif c == 2 and p == 0:
    c = 'Tesoura'
    p = 'Pedra'
    print('O JOGADOR GANHOU')
elif c == 0 and p == 1:
    c = 'Pedra'
    p = 'Papel'
    print('O JOGADOR GANHOU')
elif c == 1 and p == 0:
    c = 'Papel'
    p = 'Pedra'
    print('O COMPUTADOR GANHOU')
elif c == 1 and p == 2:
    c = 'Papel'
    p = 'Tesoura'
    print('O JOGADOR GANHOU')
elif c == 2 and p == 1:
    c = 'Tesoura'
    p = 'Papel'
    print('O COMPUTADOR GANHOU')
print('=-' * 12)
print('O computador jogou {} \nO jogador jogou {}'.format(c, p))
print('=-' * 12)

