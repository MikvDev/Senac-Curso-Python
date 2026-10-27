# Solicite quantos alunos existem em uma turma.

# Em seguida, leia a nota de cada aluno e calcule a média geral.

# A quantidade de alunos deve ser maior que zero.

#nao começe por aneiais do poder 

studentNumber = int(input("Digite a quantidade de alunos:"))
grade = 0
sum = 0
i = 1
while i <= studentNumber:
    grade = int(input(f"Digite a nota do aluno - {i}: "))
    sum += grade
    i += 1


gradeAvarage = sum / studentNumber
print(f"Media geral da turma: {gradeAvarage}:")
