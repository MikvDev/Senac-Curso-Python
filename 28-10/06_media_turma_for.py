# Leia a quantidade de alunos. Se ela for menor ou igual a zero, informe que a quantidade é inválida e não calcule a média.

# Para uma quantidade válida, utilize for para ler a nota de cada aluno. Use while para solicitar novamente qualquer nota fora da faixa de 0 a 10, sem avançar para o próximo aluno.

# Mostre a média da turma e quantos alunos obtiveram nota a partir de 7. Teste com apenas um aluno e com uma nota inválida seguida de uma válida.



numberStudents = int(input("Digite a quantidade de alunos:"))
totalGrades = 0
gradeAboveSeven = 0
if numberStudents <= 0:
    print("Numeros negativos são inválidos!")
else:
    for number in range(1,numberStudents + 1):
       nota = int(input(f"Digite a nota do aluno {number}: "))
       while nota <= 0 or nota > 10 :
            print("Digite números maiores ou iguais a 0 para a nota do aluno - numeros até 10:")
            nota = int(input(""))
       if nota > 7:
            print("Nota maior que 7!")
            gradeAboveSeven += 1
            totalGrades += nota
       
sumGradesAvarage = totalGrades / numberStudents
print("TOTAL MEDIA = ", sumGradesAvarage)
print("NOTAS MAIORES QUE 7 =", gradeAboveSeven)

    