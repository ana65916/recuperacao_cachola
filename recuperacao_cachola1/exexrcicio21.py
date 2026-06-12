# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação
print(f"\nSeu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Classificação: Magreza")
elif 18.5 <= imc < 24.9:
    print("Classificação: Normal")
elif 24.9 <= imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")