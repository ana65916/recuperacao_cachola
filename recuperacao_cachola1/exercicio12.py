nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

print("Aluno:", nome)
print("Média:", media)

if media >= 6:
    print("APROVADO(A)")
else:
    print("EM RECUPERAÇÃO")