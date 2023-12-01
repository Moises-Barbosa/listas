l = [15, 7, 27, 39]
valor = float(input("Digite o valor que deseja procurar: "))
indice = 0
for i in l:
  indice += 1
  if i == valor:
    print(f"Valor encontrado! Está no indice {indice-1}")
    indice = 0
if len(l) == indice:
  print("Valor não pertence a essa lista.")
