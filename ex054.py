from datetime import datetime
anoAtual = datetime.now().year
maiores = 0
menores = 0
for c in range (1, 8):
    p = int(input('Digite o ano de nascimento da {} pessoa: '.format(c)))
    if (anoAtual - p) >= 18:
        maiores += 1
    else:
        menores += 1
print('Ao todo tivemos {} pessoas maiores de idade, \ne também tivemos {} pessoas menores de idade.'.format(maiores, menores))