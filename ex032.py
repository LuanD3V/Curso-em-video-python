import datetime
a = int(input('Que ano quer analisar? '))
if a == 0:
    data = datetime.datetime.now()
    a = data.year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é Bissexto.'.format(a))
else:
    print('O ano {} não é Bissexto.'.format(a))