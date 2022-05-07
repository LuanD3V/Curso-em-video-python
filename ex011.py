alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2. \nPara pintar essa parede você precisará de {}l de tinta.'.format(alt, larg, alt * larg, (alt * larg)/2))