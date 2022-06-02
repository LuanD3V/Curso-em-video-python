a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if (a - b) < c < (a + b) and (b - c) < a < (b + c) and (a - c) < b < (a + c):
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b and b == c:
        print('equilátero')
    elif a == b and b != c or a == c and a != b or c == b and c != a:
        print('isóceles')
    else:
        print('escaleno')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')