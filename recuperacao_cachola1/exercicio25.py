soma = 0
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

print(f"\nA soma dos 5 números é: {soma:.2f}")