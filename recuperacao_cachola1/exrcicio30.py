soma = 0
contador = 0

while contador < 5:
    numero = float(input(f"Digite o {contador + 1}º número: "))
    soma = soma + numero
    contador = contador + 1

print(f"\nA soma dos 5 números é: {soma:.2f}")