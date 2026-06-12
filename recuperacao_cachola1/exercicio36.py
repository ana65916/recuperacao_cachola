nomes = []
gols = []

print("=== Cadastro de Jogadores ===")
for i in range(11):
    nome = input(f"\nNome do {i+1}º jogador: ")
    quantidade_gols = int(input(f"Quantidade de gols: "))
    nomes.append(nome)
    gols.append(quantidade_gols)

# Encontrar o maior número de gols
maior_gols = max(gols)
indice_artilheiro = gols.index(maior_gols)

# Resultado
print("\n=== Artilheiro do Time ===")
print(f"Nome: {nomes[indice_artilheiro]}")
print(f"Gols marcados: {gols[indice_artilheiro]}")