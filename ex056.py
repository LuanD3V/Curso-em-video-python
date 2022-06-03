mediaIdade = 0
idadeM = 0
totalF = 0
for c in range (1, 5):
    print('===== {} pessoa ====='.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    mediaIdade += idade
    if sexo == 'M' and idade > idadeM:
        idadeM = idade
        nomeM = nome
    elif sexo == 'F' and idade < 20:
        totalF += 1
print('A média de idade do grupo é de {:.1f} anos'.format(mediaIdade / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(idadeM, nomeM))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalF))
