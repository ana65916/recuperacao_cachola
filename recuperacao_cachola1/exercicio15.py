gasolina = float(input("Digite o preço da gasolina: "))
etanol = float(input("Digite o preço do etanol: "))

resultado = etanol / gasolina

if resultado >= 0.7:
    print("Compensa abastecer com gasolina.")
else:
    print("Compensa abastecer com etanol.")