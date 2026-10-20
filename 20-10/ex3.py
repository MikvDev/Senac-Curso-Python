#     Uma aplicação possui um sistema simples de autenticação.

# Considere as credenciais cadastradas:


# Solicite que a pessoa informe seu usuário e sua senha.

# O programa deverá apresentar uma das seguintes mensagens:

# Acesso autorizado! — quando ambos estiverem corretos.
# Senha incorreta! — quando o usuário estiver correto, mas a senha errada.
# Usuário não encontrado! — quando o usuário não existir.
# Desafio: Utilize condições aninhadas para verificar primeiro o usuário e depois a senha.

usuario_correto = "admin"
senha_correta = "python123"

if usuario_correto == "admin" and senha_correta == "python123":
    print(f"Bem vindo! {usuario_correto}, acesso autorizado.")
elif usuario_correto != "admin" and senha_correta == "python123":
    print("Senha ou usuário inválidos! User invalid")
elif usuario_correto == "admin" and senha_correta != "python123":
    print("Senha ou usuário inválido! Pwd invalid")
else:
    print("Dados inválidos!")
