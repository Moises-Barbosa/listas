def soma_sem_repeticao(l1, l2):
  return(set(l1 + l2))

l1 = []
l2 = []
l3 = []
for i in range(6):
  l1.append(i)
for i in range(6):
  l2.append(i+3)

l3 = (soma_sem_repeticao(l1, l2))
print(l3)
