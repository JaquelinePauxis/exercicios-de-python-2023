# import math
import random

# Solicitamos ao usuário que insira o valor da base maior do trapézio
base_maior = float(random.randint(10,100))

# Solicitamos ao usuário que insira o valor da base menor do trapézio
base_menor = float(random.randint(10,100))

# Solicitamos ao usuário que insira o valor da altura do trapézio
altura = float(random.randint(10,100))

# Calculamos a área do trapézio utilizando a fórmula (base_maior + base_menor) * altura / 2
area = (base_maior + base_menor) * altura / 2

# Imprimimos a área calculada utilizando uma f-string corretamente formatada
print(f"Valor da área do trapézio: {area:.2f}")
