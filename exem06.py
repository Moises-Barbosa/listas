fila = []
while True:
  print(f"Existem {len(fila)} cliente(s) na fila")
  print(f"Fila atual {fila}")
  print()
  print(f"Digite F para adicionar um cliente ao fim da fila ou A para a realizar o atendimento. S para sair.")
  operacao = input("Operação (F, A ou S):")

  if operacao == "F":
    print()
    cliente = input("Insira o nome do cliente:")
    fila.append(cliente)
    print()
  
  elif operacao == "A":
    if len(fila) > 0:
      print(f"Ciente -{fila[0]}- atendindo")
      fila.pop(0)
      print()
    else:
      print("A fila está vazia")
      print()
  
  elif operacao == "S":
    print("Saindo")
    break

  else:
    print("Operação inválida, tente novamente")
    print()
