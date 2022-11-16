# Faça um programa que leia a largura e altura de uma das paredes em metros, calcule a sua área e a quantidade de lata de tinta e de litros necessária para pinta-la, sabendo que cada lata de tinta contem 5 litros e pinta uma área de 2m²:

alt = float(input('Digite a altura da parede:'))
larg = float(input('Digite a largura da parede:'))
litros = float(input('Digite quantos litros uma lata possui:'))
demao = int(input('Quantas demaos vc deseja passar na parede:'))
print('Sabendo que 1 Litro de tinta rende 2m²')


a = alt*larg
t = (a/2)*demao

if (a % 2) > 0 and t > litros:
    l = (t//litros)+1
else:
    l = (t/litros)

if l > 1:
    s = 'latas'
else:
    s = 'lata'


print('A área da parede é {:.2f} \nVocê usará {:.2f} litros de tinta\nVocê precisará comprar {} {} de tinta'.format(
    a, t, (round(l)), s))
