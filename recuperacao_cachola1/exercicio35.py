senha = []

print("Digite uma senha com 6 vogais (a, e, i, o, u):")
for i in range(6):
    while True:
        caractere = input(f"{i+1}º caractere: ").lower()
        if caractere in "aeiou":
            senha.append(caractere)
            break
        else:
            print("Digite apenas vogais!")

# Criptografia
senha_cripto = []
for letra in senha:
    if letra == 'a':
        senha_cripto.append('z')
    elif letra == 'e':
        senha_cripto.append('3')
    elif letra == 'i':
        senha_cripto.append('l')
    elif letra == 'o':
        senha_cripto.append('0')
    elif letra == 'u':
        senha_cripto.append('$')

# Resultado
print(f"\nSenha digitada: {''(senha)}")
print(f"Senha criptografada: {''(senha_cripto)}")