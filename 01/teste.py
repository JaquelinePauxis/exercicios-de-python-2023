# Solicitamos ao usuário que insira o valor da base maior do trapézio
base_maior = float(input("Digite o valor da base maior: "))

# Solicitamos ao usuário que insira o valor da base menor do trapézio
base_menor = float(input("Digite o valor da base menor: "))

# Solicitamos ao usuário que insira o valor da altura do trapézio
altura = float(input("Digite o valor da altura: "))

# Calculamos a área do trapézio utilizando a fórmula (base_maior + base_menor) * altura / 2
area = (base_maior + base_menor) * altura / 2

# Imprimimos a área calculada utilizando uma f-string para formatar a mensagem
print(f"Valor da área do trapézio: {area}")