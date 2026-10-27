# Parte 3 — Reflexão individual
Cada integrante deve escrever um parágrafo de 5 a 8 linhas respondendo:

Como o filme e os programas desta atividade ajudam a compreender a relação entre regras, testes e decisões humanas? Cite uma condição do seu código e explique um limite da simulação.

O Filme Jogo da imitação e os programas resolvidos ajudam a compreender como funciona o passo a passo de um algoritmo para ser executado. Sendo assim, precisamos tratar exceções, erros e ações que o usuário venha a fazer em nosso sistema. 

Em nosso código do exercicio 2:
Temos a validação 
```

if timeRemaning <= 0 or timeNecessary <= 0:
    print("Tempo inválido.")

```

Nela evitamos que o usuário digite um valor negativo de tempo. O Limite da simulação em comparação com nosso código e o filme é que em nosso programa ele não traduz frases criptografadas, apenas simulamos a quantidade de grupos de códigos, e tempo necessário para que o analista consiga realizar uma descriptação.