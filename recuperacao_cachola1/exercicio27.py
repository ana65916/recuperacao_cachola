contador = 0
for i in range(12):
    altura = float(input(f"Digite a altura do {i+1}º atleta (em metros): "))
    if altura > 1.90:
        contador += 1

print(f"\nQuantidade de atletas com mais de 1,90m: {contador}")