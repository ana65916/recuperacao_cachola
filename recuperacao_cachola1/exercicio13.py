
quantidade = int(input("Digite a quantidade de sucos: "))

if quantidade > 10:
    preco = 4.50
else:
    preco = 5.50

total = quantidade * preco

print("Valor a pagar: R$", total)