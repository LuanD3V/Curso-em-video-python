from random import randint


from time import sleep
print('-=' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=' * 20)
n = int(input('Em que número eu pensei? '))
c = randint(0, 5)
print('Processando...')
sleep(2)
if n != c:
    print('GANHEI, eu pensei no número {} e não no {}.'.format(c, n))
else:
    print('PERDI, eu pensei no número {}, e você também.'.format(c))
