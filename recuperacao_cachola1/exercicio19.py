# Solicita a estação desejada
estacao = input("Digite a estação do ano (outono, inverno, primavera ou verão): ").lower()

# Exibe a data de início
if estacao == "outono":
    print("Outono começa em: 20 de março")
elif estacao == "inverno":
    print("Inverno começa em: 21 de junho")
elif estacao == "primavera":
    print("Primavera começa em: 22 de setembro")
elif estacao == "verão":
    print("Verão começa em: 21 de dezembro")
else:
    print("Estação inválida! Digite corretamente.")