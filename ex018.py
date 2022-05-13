from math import cos, sin, tan, radians
a = float(input('Digite o ângulo que você deseja: '))
r = radians(a)
print('O ângulo de {} tem o seno de {:.2f}. \nO ângulo de {} tem o cosseno de {:.2f}. \nO ângulo de {} tem a tangente de {:.2f}.'.format(a, sin(r), a, cos(r), a, tan(r)))