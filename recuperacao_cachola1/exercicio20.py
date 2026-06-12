# Solicita uma vogal e padroniza para minúscula
vogal = input("Digite uma vogal: ").lower()

# Verifica se é realmente uma vogal e mostra exemplos
if vogal in "aeiou":
    if vogal == "a":
        print("Palavras com A: Abacaxi, Amigo, Árvore")
    elif vogal == "e":
        print("Palavras com E: Escola, Elefante, Estrela")
    elif vogal == "i":
        print("Palavras com I: Ilha, Índio, Igreja")
    elif vogal == "o":
        print("Palavras com O: Ovo, Orelha, Olho")
    elif vogal == "u":
        print("Palavras com U: Urso, Unha, União")
else:
    print("Não é uma vogal válida! Digite A, E, I, O ou U.")