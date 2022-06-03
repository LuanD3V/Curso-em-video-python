s = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        s += c
print('A soma dos valores é {}.'.format(s))