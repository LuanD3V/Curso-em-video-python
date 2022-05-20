p1 = int(input('Digite o primeiro valor: '))
p2 = int(input('Digite o segundo valor: '))
p3 = int(input('Digite o terceiro valor: '))
if p1 < p2 and p1 < p3:
    menor = p1
elif p2 < p1 and p2 < p3:
    menor = p2
else:
    menor = p3
print('O menor valor digitado foi {}'.format(menor))
if p1 > p2 and p1 > p3:
    maior = p1
elif p2 > p1 and p2 > p3:
    maior = p2
else:
    maior = p3
print('O maior número digitado foi {}'.format(maior))
