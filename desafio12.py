#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n1 = float(input('Digite um número:'))
n2 = float(input('Digite a porcentagem que deseja:'))
n3 = str(input('Digite D se deseja ver o valor com desconto ou J se deseja ver o valor com Juros ou A se deseja ver ambos:').upper())

if n3 in 'J' or n3 in 'A':
    s1 = n1 * (1+(n2/100))
    print('O valor com juros é {:.2f}'.format(s1))

if n3 in 'D' or n3 in 'A':
    s2 = n1 * (1-(n2/100))
    print('O valor com desconto é {:.2f}'.format(s2))

