# Solicitamos ao usuário que insira o valor da base maior do trapézio
base_maior = float(input("Digite o valor da base maior: "))

# Solicitamos ao usuário que insira o valor da base menor do trapézio
base_menor = float(input("Digite o valor da base menor: "))

# Solicitamos ao usuário que insira o valor da altura do trapézio
altura = float(input("Digite o valor da altura: "))

# Calculamos a área do trapézio utilizando a fórmula (base_maior + base_menor) * altura / 2
area = (base_maior + base_menor) * altura / 2

# Imprimimos a área calculada utilizando uma f-string corretamente formatada
print(f"Valor da área do trapézio: {area}")


Peça aos alunos que modifiquem o código para calcular a área de dois trapézios diferentes, com valores diferentes de bases e altura.
Eles devem executar o código e verificar se os resultados estão corretos.
conceitos a serem apresentados:

float = docstrings
input()
f-strings : print(f"Valor da área do trapézio: {area}")

	A f-string torna a formatação de saídas mais legível e conveniente, especialmente quando você precisa mesclar texto com valores de variáveis.
Ela permite incorporar valores de variáveis dentro de strings de maneira direta e concisa, facilitando a interpolação de valores em texto.

print("Valor da área do trapézio: " + str(area))

Conversão para String: Como area é um valor numérico, você precisa convertê-lo explicitamente para uma string usando a função str() antes de concatená-lo com o texto. Isso garante que o valor numérico seja tratado como uma string.


Eficiência: A concatenação de strings usando + pode ser menos eficiente em termos de desempenho, especialmente quando você está concatenando várias strings. Isso ocorre porque cada concatenação cria uma nova string, resultando em alocações e cópias adicionais de memória. As f-strings são mais eficientes nesse aspecto.
Legibilidade: As f-strings são mais legíveis, pois permitem que você insira diretamente os valores das variáveis na string, tornando mais claro o que está sendo inserido onde.
Portanto, embora a reescrita seja possível, o uso de f-strings é geralmente mais recomendado por sua legibilidade e eficiência.


=

1. `=` (Atribuição):
   O sinal de igual (`=`) é usado para atribuição em muitas linguagens de programação, incluindo Python. Ele é usado para associar um valor a uma variável. Por exemplo:
   
   ```python
   x = 10
   nome = "Alice"
   ```

   Nesses exemplos, o valor `10` é atribuído à variável `x`, e o valor `"Alice"` é atribuído à variável `nome`.



== 
2. `==` (Igualdade):
   O operador de igualdade (`==`) é usado para comparar se dois valores são iguais. Ele retorna `True` se os valores forem iguais e `False` caso contrário. Por exemplo:
   
   ```python
   x = 5
   y = 10
   resultado = x == y  # Isso resultará em False
   ```

   Nesse exemplo, a variável `resultado` receberá o valor `False`, porque `x` e `y` são diferentes.




===
3. `===` (Comparação Estrita - em algumas linguagens):
   O operador `===` é usado em algumas linguagens de programação para verificar igualdade estrita, o que significa que ele verifica não apenas se os valores são iguais, mas também se os tipos são os mesmos. No entanto, em muitas linguagens, como Python, esse operador não é usado; em vez disso, apenas `==` é usado para verificar a igualdade entre valores.

# 2.f#
Cada um desses sinais tem um propósito específico em programação, e seu uso varia de acordo com a linguagem que você está utilizando. Certifique-se de entender o contexto em que eles são usados para evitar confusões.

O .2f é um especificador de formato usado em strings formatadas (f-strings) no Python. Ele é usado para controlar como um número de ponto flutuante será formatado quando exibido como uma string. Vou quebrar isso em partes:

O : indica que estamos especificando um formato para o valor que vem em seguida.
O .2 especifica o número de casas decimais que queremos mostrar após o ponto.
O f indica que o valor é um número de ponto flutuante.
Portanto, :.2f está dizendo ao Python para formatar o número de ponto flutuante com duas casas decimais após o ponto. Isso é útil para controlar a precisão da saída quando estamos trabalhando com números de ponto flutuante, como no cálculo da área do trapézio, para mostrar resultados com um número específico de casas decimais.

Por exemplo, se o valor calculado da área for 25.6789, usar {area:.2f} fará com que seja exibido como "25.68", arredondado para duas casas decimais. Isso torna a saída mais legível e evita mostrar muitos dígitos após o ponto decimal.