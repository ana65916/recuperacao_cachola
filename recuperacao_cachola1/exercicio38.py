# Função para reajustar gasolina
def reajustar_gasolina(preco, valor_reajuste):
    return preco + valor_reajuste

# Função para reajustar etanol (também retorna o ajuste extra da gasolina)
def reajustar_etanol(preco_etanol, valor_reajuste):
    novo_etanol = preco_etanol + valor_reajuste
    ajuste_extra_gasolina = valor_reajuste * 0.27  # 27% do reajuste do etanol
    return novo_etanol, ajuste_extra_gasolina

# Programa principal
preco_gasolina = float(input("Digite o preço atual da gasolina: R$ "))
preco_etanol = float(input("Digite o preço atual do etanol: R$ "))
valor_reajuste = float(input("Digite o valor do reajuste: R$ "))
combustivel = input("Qual combustível receberá o reajuste? (G - Gasolina / E - Etanol): ").upper()

# Processa o reajuste
if combustivel == "G":
    preco_gasolina = reajustar_gasolina(preco_gasolina, valor_reajuste)

elif combustivel == "E":
    preco_etanol, ajuste_extra = reajustar_etanol(preco_etanol, valor_reajuste)
    preco_gasolina = preco_gasolina + ajuste_extra  # Aplica os 27% na gasolina

else:
    print("Combustível inválido!")

# Exibe o resultado final
print("\n=== Preços atualizados ===")
print(f"Gasolina: R$ {preco_gasolina:.2f}")
print(f"Etanol: R$ {preco_etanol:.2f}")