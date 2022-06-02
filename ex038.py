from smtpd import MailmanProxy


n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O primeiro valor {} é maior.'.format(n1))
elif n1 < n2:
    print('O segundo valor {} é maior.'.format(n2))
elif n1 == n2:
    print('Não existe valor maior, os dois valores {} e {} são iguais.'.format(n1, n2))
else:
    print('Valor incorreto, tente novamente!')