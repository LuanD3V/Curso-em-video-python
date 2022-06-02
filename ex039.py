import datetime
ano = int(input('Qual o seu ano de nascimento? '))
anoAtual = datetime.datetime.now().year
idade = anoAtual - ano
if idade == 18:
    print('Você tem {} anos, e precisa se alistar agora no exército.'.format(idade))
elif idade == 17:
    print('Você tem {} anos, e precisa se alistar ano que vem no exército.'.format(idade))
elif idade < 17:
    print('Você tem {} anos, e irá se alistar no exército em {}.'.format(idade, 18 + ano))
elif idade > 18:
    print('Você tem {} anos, e já passou do tempo de se alistar, o seu ano foi em {}.'.format(idade, ano + 18))
else:
    print('Valor inválido, tente novamente!')