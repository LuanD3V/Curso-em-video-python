n = int(input('Digite um número para saber se é primo: '))
total = 0
for c in range (1, n + 1):
    if n % c == 0:
        total += 1
print('O número {} foi divisível {} vezes'.format(n, total))
if total == 2:
    print('e por isso é um número primo')
else:
    print('e por isso não é um número primo')