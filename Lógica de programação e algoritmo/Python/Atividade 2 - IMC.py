altura = float(input('Digite a altura: '))
peso = float(input('Digite o seu peso:'))

soma = altura * altura
imc = peso / (altura * altura)

print('O seu IMC é: {:.2f}'.format(imc))
 