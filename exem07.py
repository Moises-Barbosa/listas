fila = []
executar = True
while executar:
  print(f"Existem {len(fila)} cliente(s) na fila")
  print(f"Fila atual {fila}")
  print()
  print(f"Digite F para adicionar um cliente ao fim da fila ou A para a realizar o atendimento. S para sair.")
  operacao = input("Operação (F, A, S ou FFFAAS):")
  
  for letra in operacao:
    if letra == "F":
      print()
      cliente = input("Insira o nome do cliente:")
      fila.append(cliente)
      print()
  
    elif letra == "A":
      if len(fila) > 0:
        print(f"Ciente -{fila[0]}- atendindo")
        fila.pop(0)
        print()
      else:
        print("A fila está vazia")
        print()
  
    elif letra == "S":
      print("Saindo")
      executar = False
      break

    else:
      print("Operação inválida, tente novamente")
