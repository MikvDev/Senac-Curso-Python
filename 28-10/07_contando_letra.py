# Leia uma palavra e, depois, uma única letra. Percorra a palavra diretamente com for e conte quantas vezes a letra aparece.

# Considere que o usuário informará exatamente um caractere na segunda entrada. Diferencie maiúsculas e minúsculas: a e A são valores distintos.

# Teste com banana e a (resultado 3), com uma letra ausente e com uma palavra vazia.
word = input("Digite uma palavra:")
letterInWord  = input("Digite uma letra:")
isLetterFound = 0
for letter in word:
    if letter == letterInWord:
        print("letra encontrada!")
        isLetterFound += 1

print("PALAVRA = ", word)
print("LETRA - apareceu ", isLetterFound, "vezes" )
    
    
