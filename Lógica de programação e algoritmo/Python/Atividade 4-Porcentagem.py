numero = int(input ("Digite um número de [1 a 10000]:" ))
porcentagem = int(input("Digite uma porcentagem de [1 a 100]: "))

resultado = numero * (porcentagem / 100)

print(f"O resultado é: {round(resultado, 2)}")