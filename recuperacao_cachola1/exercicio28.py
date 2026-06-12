soma = 0
maior = -1
menor = 11  # Notas de 0 a 10

for i in range(25):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    soma += nota
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

media = soma / 25
print(f"\nMaior nota: {maior:.1f}")
print(f"Menor nota: {menor:.1f}")
print(f"Média da turma: {media:.2f}")