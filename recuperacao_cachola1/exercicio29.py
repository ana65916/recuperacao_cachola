# Exercício 36 completo
quantidade_correta = 82

print("Adivinhe quantas bolinhas de gude há no pote!")
print("Você tem 5 tentativas.\n")

# Laço para 5 tentativas
for tentativa in range(1, 6):
    palpite = int(input(f"Tentativa {tentativa}/5: Digite o número: "))

    if palpite == quantidade_correta:
        print(" Parabéns, você acertou!")
        break  # Encerra o programa se acertar
    elif palpite < quantidade_correta:
        print(" Você errou! Existem mais bolinhas do que você digitou.\n")
    else:
        print(" Você errou! Existem menos bolinhas do que você digitou.\n")
else:
    # Executa se acabar as 5 tentativas sem acertar
    print(f" Suas tentativas acabaram! O número correto era {quantidade_correta}.")