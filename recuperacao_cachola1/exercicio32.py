# Inicializa variáveis
maior_velocidade = 0
menor_velocidade = float('inf')
nome_rapido = ""
nome_lento = ""
soma_velocidades = 0
quantidade_pilotos = 0

# Pergunta se quer continuar
continuar = input("Deseja cadastrar um piloto? (S/N): ").upper()

while continuar == "S":
    nome = input("Digite o nome do piloto: ")
    velocidade = float(input("Digite a velocidade da volta (km/h): "))

    # Atualiza soma e contador
    soma_velocidades = soma_velocidades + velocidade
    quantidade_pilotos = quantidade_pilotos + 1

    # Verifica volta mais rápida
    if velocidade > maior_velocidade:
        maior_velocidade = velocidade
        nome_rapido = nome

    # Verifica volta mais lenta
    if velocidade < menor_velocidade:
        menor_velocidade = velocidade
        nome_lento = nome

    continuar = input("\nCadastrar outro piloto? (S/N): ").upper()

# Exibe resultados se houver pilotos
if quantidade_pilotos > 0:
    media = soma_velocidades / quantidade_pilotos
    print("\n=== Resultados ===")
    print(f"Piloto mais rápido: {nome_rapido} | Velocidade: {maior_velocidade:.2f} km/h")
    print(f"Piloto mais lento: {nome_lento} | Velocidade: {menor_velocidade:.2f} km/h")
    print(f"Média de velocidade: {media:.2f} km/h")
else:
    print("Nenhum piloto foi cadastrado.")