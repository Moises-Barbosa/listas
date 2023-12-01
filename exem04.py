#1º forma
def soma(l1, l2):
  return l1 + l2

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = []

l3 = (soma(l1, l2))
print(l3)
print()

#2º forma
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = []

l3.extend(l1)
l3.extend(l2)
print(l3)
print()

#3º forma
l1 = []
l2 = []
l3 = []

for i in range(5):
  l1.append(i+1)
for i in range(5):
  l2.append(i+6)

l3 = (soma(l1, l2))
print(l3)
