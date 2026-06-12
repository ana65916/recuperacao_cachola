# Solicita a letra e padroniza para maiúscula
letra = input("Digite a letra do suco (L, M, A ou U): ").upper()

# Verifica a opção e exibe o resultado
if letra == "L":
    print("Suco: Laranja | Principal vitamina: C")
elif letra == "M":
    print("Suco: Morango | Principal vitamina: A")
elif letra == "A":
    print("Suco: Acerola | Principal vitamina: C")
elif letra == "U":
    print("Suco: Uva | Principal vitamina: E")
else:
    print("Letra inválida! Escolha entre L, M, A ou U.")