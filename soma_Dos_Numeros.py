# Inicializa as variáveis de soma e contador
soma = cont = 0

# Laço infinito para continuar pedindo números até o usuário digitar 00
while True:
    # Solicita ao usuário digitar um número
    num = float(input("Digite um número: [00 para parar] "))
    
    # Verifica se o número digitado é 00, para interromper o laço
    if num == 00:
        break  # Encerra o laço se o número for 000
    
    # Adiciona o número à soma
    soma += num
    # Incrementa o contador de números
    cont += 1

# Exibe a soma dos números digitados e a quantidade de números
print(f"A soma dos {cont} números é {soma}.")