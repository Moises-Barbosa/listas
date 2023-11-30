notas = [0, 0, 0, 0, 0]
soma = 0
for i in notas:
  nota = float(input("Adicione a nota do aluno:"))
  soma += nota
print(soma/len(notas))