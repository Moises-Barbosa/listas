lista = []
abertura_esquerda = 0
abertura_direita = 0
parenteses = input("Insira os parênreses:")
for letra in parenteses:
  lista.append(letra)
  if letra == "(":
    abertura_direita += 1
  elif letra == ")":
    abertura_esquerda += 1
  else:
    print("Digite somente parênteses")

if abertura_direita != abertura_esquerda:
  print("ERRO")
elif lista[0] == ")":
  print("ERRO")
elif lista[-1] == "(":
  print("ERRO")
else:
  print("OK")

