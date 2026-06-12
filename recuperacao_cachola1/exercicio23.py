# Preços definidos
preco_pao = 0.80
preco_queijo = 5.00
preco_bisnaga = 3.50
preco_leite = 4.20
preco_doce = 2.50
preco_suspiro = 1.80

# Entrada de quantidades
qtd_pao = int(input("Quantidade de pães: "))
qtd_queijo = int(input("Quantidade de queijos: "))
qtd_bisnaga = int(input("Quantidade de bisnagas: "))
qtd_leite = int(input("Quantidade de leites: "))
qtd_doce = int(input("Quantidade de doces: "))
qtd_suspiro = int(input("Quantidade de suspiros: "))

# Cálculo do valor total sem desconto
total = (qtd_pao * preco_pao) + (qtd_queijo * preco_queijo) + \
        (qtd_bisnaga * preco_bisnaga) + (qtd_leite * preco_leite) + \
        (qtd_doce * preco_doce) + (qtd_suspiro * preco_suspiro)

# Verificação do maior desconto
desconto = 0
if qtd_pao >= 10 and qtd_queijo >= 1:
    desconto = max(desconto, 10)
if qtd_bisnaga >= 1 or qtd_pao >= 1:
    desconto = max(desconto, 15)
if (qtd_leite >= 1 and qtd_doce >= 1) or qtd_suspiro >= 1:
    desconto = max(desconto, 5)

# Aplicação do desconto
valor_com_desconto = total * (1 - desconto / 100)

# Resultado
print(f"\nValor total: R$ {total:.2f}")
if desconto > 0:
    print(f"Desconto aplicado: {desconto}%")
else:
    print("Nenhum desconto aplicado")
print(f"Valor final a pagar: R$ {valor_com_desconto:.2f}")