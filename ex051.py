pt = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
d = pt + (10 - 1) * r
for c in range (pt, d + r, r):
    print(c)