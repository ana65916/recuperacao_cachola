# Entrada de dados
idade = int(input("Digite sua idade: "))
tempo_carteira = int(input("Tempo de habilitação (anos): "))
tipo_carteira = input("Tipo de carteira que possui (B ou C): ").upper()
infracao = input("Teve infração nos últimos 12 meses? (S/N): ").upper()

# Verificação das regras
apto = False

if idade > 21:
    if (tipo_carteira == "B" and tempo_carteira >= 2) or (tipo_carteira == "C" and tempo_carteira >= 1):
        if infracao == "N":
            apto = True

# Resultado
if apto:
    print("\nVocê está APTO para tirar a carteira tipo D!")
else:
    print("\nVocê NÃO está apto para tirar a carteira tipo D.")