frase = str(input('Digite a frase para saber se é Palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertido = ''
for letra in range (len(junto) - 1, - 1, -1):
    invertido += junto[letra]
if invertido == junto:
    print('A frase é um Palíndromo')
else: 
    print('A frase não é um Palíndromo')

