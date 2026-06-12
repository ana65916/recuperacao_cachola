# Entrada de dados
nota_teste = float(input("Digite a nota do teste: "))
nota_prova = float(input("Digite a nota da prova: "))
faltas = int(input("Digite a quantidade de faltas: "))

# Cálculo da média
media = (nota_teste + nota_prova) / 2

# Verificação da situação
print(f"\nMédia final: {media:.1f}")
if media >= 7.0 and faltas < 10:
    print("Situação: Aprovado")
elif 5.0 <= media < 7.0 and faltas < 10:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")
    