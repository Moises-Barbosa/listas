numeros = [0, 0, 0, 0, 0]

for i in range(len(numeros)):
  numeros[i] = float(input("Qual é o numero?"))

posicao = int(input("Qual a posição do numero?"))
print(f"{numeros[posicao - 1]:.0f}")