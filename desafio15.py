# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quaios ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.


n1 = float(input('Quantos dias você alugou o carro?'))
n2 = float(input('Quantos kilómetros você percorreu com o carro?'))

s1 = n1 * 60
s2 = n2 * 0.15
s3 = s1 + s2

print('-'*15, 'Valor por itens:','-'*15)
print('O valor gasto por dias alugados é: R${:.2f} \nO valor gasto por KM é: R${:.2f} \nValor total: R${:.2f}'.format(s1,s2,s3))
