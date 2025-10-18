# Inicializa as variáveis para contagem e soma
num = cont = soma = 0

# Solicita o primeiro número ao usuário
num = float(input("Digite um numero: [00 para parar] "))

# Enquanto o número digitado não for 999, o laço continua
while num != 00:
    cont += 1  # Incrementa a quantidade de números digitados
    soma += num  # Soma o número ao total
    num = float(input("Digite um numero: [00 para parar] "))  # Solicita o próximo número

# Exibe a quantidade de números digitados e a soma total
print(f"Você digitou {cont} números, o total foi {soma:.2f}!")
