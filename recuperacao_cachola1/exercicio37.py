# Função que altera o valor por referência (usando lista)
def dobrar_valor(valor_ref):
    valor_ref[0] = valor_ref[0] * 2  # Altera o valor dentro da lista

# Programa principal
numero = int(input("Digite um número: "))
valor = [numero]  # Usamos lista para simular passagem por referência

dobrar_valor(valor)

print(f"O dobro do número é: {valor[0]}")