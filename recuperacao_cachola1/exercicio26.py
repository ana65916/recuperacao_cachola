contador = 0
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero > 50:
        contador += 1

print(f"\nQuantidade de números maiores que 50: {contador}")