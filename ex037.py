n = int(input('Digite um valor inteiro: '))
c = int(input('Escolha uma das opções pelo número: \n1 - Binário \n2 - Octal \n3 - Hexadecimal \n'))
if c == 1:
    c = bin(n)
elif c == 2:
    c = oct(n)
elif c == 3:
    c = hex(n)
else:
    print('Valor Incorreto, tente novamente!')
print('O número {} convertido é {}.'.format(n, c [2:]))