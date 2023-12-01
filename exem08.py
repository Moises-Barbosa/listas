fila1 = []
fila2 = []
executar = True

while executar:
  print(f"A fila 1 possui {len(fila1)} clientes")
  print(f"Clientes na fila 1: {fila1}")
  print(f"A fila 2 possui {len(fila2)} clientes")
  print(f"Clientes na fila 2: {fila2}")
  fila = input(f"Selecione a fila (1 ou 2):")
  if fila == "1":
    opcao = input("Digite F para adicionar um cliente, A para atender e S para sair (exemplo: FFA)")
    for letra in opcao:
      if letra == "F":
        fila1.append(input("Digite o nome do cliente:"))
      elif letra == "A":
        if len(fila1) > 0:
          atendido = fila1.pop(0)
          print(f"cliente --{atendido}-- atendido")
        else:
          print("Fila vazia")
      elif letra == "S":
        print("Saindo")
        executar = False
      else:
        print("Opção inválida, digite novamente")
  else:
    opcao = input("Digite F para adicionar um cliente, A para atender e S para sair (FFA)")
    for letra in opcao:
      if letra == "F":
        fila2.append(input("Digite o nome do cliente:"))
      elif letra == "A":
        if len(fila2) > 0:
          print(f"Cliente --{fila2[0]}-- atendido")
          fila2.pop(0)
        else:
          print("Fila vazia")
      elif letra == "S":
        print("Saindo")
        executar = False
      else:
        print("Opção inválida, digite novamente")