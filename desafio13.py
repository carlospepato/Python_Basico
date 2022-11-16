#Faça um programa que converta a temperatura em qualquer unidade de medida '°C,F,K

n1 = str(input('Digite primeiramente a unidade de medida da temperatura "C,K,F":')).upper()
n2 = float(input("Digite o valor da temperatura:"))
n3 = str(input('Digite a unidade de medida que deseja converter "C,K,F:')).upper()

if n1 in 'C' and n3 in 'F':
    if n2 < -273.15:
        print('Temperatura inexistente')
    else:
        s1 = (n2*9/5) +32
        print('A temperatura é {:.2f}°F'.format(s1))

if n1 in "F" and n3 in 'C':
    if n2 < -459.67:
        print('Temperatura inexistente')
    else:
        s2 = (n2 - 32)*5/9
        print('A temperatura é {:.2f}°C'.format(s2))

if n1 in 'C' and n3 in 'K':
    if n2 < -273.15:
        print('Temperatura inexistente')
    else:
        s3 = n2 + 273.15
        print('A temperatura é {:.2f}K'.format(s3))

if n1 in "K" and n3 in 'C':
    if n2 < 0:
        print('Temperatura inexistente')
    else:
        s4 = n2 - 273.15
        print('A temperatura é {:.2f}°C'.format(s4))

if n1 in 'F' and n3 in 'K':
    if n2 < -459.67:
        print('Temperatura inexistente')
    else:
        s5 = ((n2 -32)*5/9) + 273.15
        print('A temperatura é {:.2f}K'.format(s5))

if n1 in "K" and n3 in 'F':
    if n2 < 0:
        print('Temperatura inexistente')
    else:
        s6 = ((n2 - 273.15)*9/5)+32
        print('A temperatura é {:.2f}°F'.format(s6))
