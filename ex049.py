n = int(input('Digite um número para ver sua tabuada: '))
op = int(input('''Digite a tabuada desejada
[1] Para Somar
[2] Para Multiplicar
[3] Para Subtrair
[4] Para Dividir
: '''))
if op == 1:
    for c in range (0, 11):
        print('{} + {} = {}'.format(n, c, n + c))
elif op == 2:
    for c in range (0, 11):
        print('{} x {} = {}'.format(n, c, n * c))
elif op == 3:
    for c in range (0, 11):
        print('{} - {} = {}'.format(n, c, n - c))
elif op == 4:
    for c in range (0, 11):
        print('{} / {} = {}'.format(n, c, n / c))
else:
    print('Valor inválido, tente novamente!')
