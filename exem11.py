l = [15, 7, 27, 39]
v1 = float(input("Digite o primeiro valor que deseja procurar: "))
v2 = float(input("Digite o segundo valor que deseja procurar: "))
indice = 0
for i in l:
  indice += 1
  if i == v1:
    print(f"Primeiro valor encontrado! Está no indice {indice - 1}.")
    break
  elif indice == len(l):
    print("O primeiro valor não pertence a essa lista.")
indice = 0
for i in l:
  indice += 1
  if i == v2:
    print(f"Segundo valor encontrado! Está no indice {indice - 1}")
    break
  elif indice == len(l):
    print("O segundo valor não pertence a essa lista.")