# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar:  Considere US$1,00 - R$3,27

q = str(input('Digite R se for Real ou D se for Dolar:'))


if q in 'R' or q in 'r':
    n1 = float(input('Quantos reais você deseja investir:'))
    real = float(input('Quanto está custando o dolar:'))
    res1 = n1/real
    print('Você comprará {:.2f} dolares'.format(res1))


if q in 'D' or q in 'd':
    n2 = float(input('Quantos Dolares você deseja investir:'))
    dolar = float(input('Quanto está custando o dolar:'))
    res2 = n2*dolar
    print('Você comprará {:.2f} Reais'.format(res2))
