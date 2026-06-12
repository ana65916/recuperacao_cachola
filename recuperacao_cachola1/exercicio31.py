soma = 0
quantidade = 0

while soma < 100:
    numero = float(input("Digite um número: "))
    soma = soma + numero
    quantidade = quantidade + 1

print(f"\nQuantidade de números necessários: {quantidade}")
print(f"Soma total alcançada: {soma:.2f}")