# Lista para armazenar os valores das refeições
cartela = []

print("=== Programa de Fidelização ===")

while len(cartela) < 10:
    valor = float(input(f"Digite o valor da {len(cartela)+1}ª refeição: R$ "))
    cartela.append(valor)

# Ao completar 10 valores
print("\nHoje o seu almoço é uma cortesia da casa, Parabéns!")