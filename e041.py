from datetime import date
idade = int(input('Qual ano você nasceu? '))
idade = date.today().year - idade
if idade <= 9:
    classe = 'Junior'
elif idade <= 14:
    classe = 'Infantil'
elif idade <= 19:
    classe = 'Junior'
elif idade <= 25:
    classe = 'Sênior'
elif idade > 25:
    classe = 'Master'
else:
    print('Valor inválido! Tente novamente.')
print('O Atleta tem {} anos. \nClassificação: {}.'.format(idade, classe))
