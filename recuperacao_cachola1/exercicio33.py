velocidades = []
contador = 0

while contador < 6:
    vel = float(input(f"Digite a velocidade da {contador + 1}ª volta (km/h): "))
    velocidades.append(vel)
    contador += 1

print("\n=== Velocidades registradas ===")
i = 0
while i < 6:
    print(f"Volta {i + 1}: {velocidades[i]:.2f} km/h")
    i += 1

maior = max(velocidades)
menor = min(velocidades)
media = sum(velocidades) / 6

print(f"\nVolta mais rápida: {maior:.2f} km/h")
print(f"Volta mais lenta: {menor:.2f} km/h")
print(f"Média das velocidades: {media:.2f} km/h")