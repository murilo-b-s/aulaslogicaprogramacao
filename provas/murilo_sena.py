"""      MURILO BRUM SENA      """


"""

Enunciado:
Utilizando o menu a baixo, desenvolva o código necessário conforme
as instruções:

Na opção 1, você deverá 'cadastrar' o login e a senha de uma pessoa.
Obs: - Você deverá realizar a confirmação da senha antes de 
salvar na lista de senhas (lst_senhas) e na lista de logins 
(lst_logins).
Caso as duas senhas não sejam iguais, avisar o usuário e permitir
a digitação novamente da senha e novamente a confirmação.
- Permita apenas 3 tentativas. Volte ao Menu.
- O login deve ser único, a senha pode repetir.

Na opção 2, você deverá testar se o login e a senha estão funcionando
corretamente. Se estiver, avise que está tudo ok. 

Na opção 3, você deverá possibilitar a troca de senha de um usuário.
Para isso, leia o login, e a senha antiga. 
Se estiver OK, aceite a nova senha. 
Obs: Não esqueça de validar novamente a senha.

Na opção 4, você deverá implementar a exclusão de um login e também 
da senha correspondente. 
"""

# Sua tarefa é desenvolver o que falta no código abaixo.

menu = """
    ================================
    0- Finaliza o código
    1- Cadastrar login e senha
    2- Validar login e senha
    3- Alterar a senha
    4- Excluir um login
    ================================
"""


def c():
    while True:
        login = input("Digite o seu nome de usuário:")
        if login == "":
            print("Nome de usuário vazio.")
            continue
        if login in lst_logins:
            print("Esse nome de usuário já existe: ")
            continue
        lst_logins.append(login)
        break
    return login



lst_logins = ['murilo22', 'caio4o', 'murilo']
lst_senhas = ['abc', 'cbd', 'mur']

while True:
    print(menu)
    escolha = input("    Escolha: ")

    if escolha == "0":
        break
        
    if escolha == "1":
        while True:
            c():
            break
        
        i = 1
        while i <= 3:
            
            senha = input("Digite a sua senha: ")
            if senha == "":
                print("A senha não pode ficar vazia. Digite uma senha válida: ")
                continue
            
            print("Confirme a sua senha: ")
            senha_conf = input()
            if senha_conf == senha:
                lst_senhas.append(senha)
                print("Senha confirmada!")
            else:
                print("Senha incorreta: ")
                i += 1
                continue
            break        
        
    if escolha == "2":
        while True:
            nome = input("Nome de usuário: ")
            if nome in lst_logins:
                indice = lst_logins.index(nome)
            else:
                print("Nome de usuário não encontrado: ")
                continue
        
            senha = input("Senha:")
            if senha == lst_senhas[indice]:
                print("Está tudo certo com o seu login!")
            else:
                print("senha incorreta. Login inválido")
            break    
        
    if escolha == "3":
        while True:
            nome = input("Nome de usuário: ")
            if nome in lst_logins:
                indice = lst_logins.index(nome)
            else:
                print("Nome de usuário não encontrado: ")
                continue
            
            senha = input("Senha:")
            if senha == lst_senhas[indice]:
                while True:
                    nova_senha = input("Digite a sua senha nova: ")
                    if nova_senha == "":
                        print("A senha não pode ficar vazia. Digite uma senha válida: ")
                        continue
            
                    print("Confirme a sua senha: ")
                    senha_conf = input()
                    if senha_conf == nova_senha:
                        lst_senhas[indice] = nova_senha
                        print("Senha substituida!")
                        break
                    else:
                        print("Senha incorreta: ")
                        continue
            else:
                print("Senha incorreta.")
                continue
            break
                
    if escolha == "4":
        while True:
            nome = input("Login que deseja excluir: ")
            if nome in lst_logins:
                indice = lst_logins.index(nome)
            else:
                print("Nome de usuário não encontrado: ")
                continue
            
            senha = input("Senha:")
            if senha == lst_senhas[indice]:
                print("Este login foi excluido.")
                
            else:
                print("senha incorreta. Login inválido")
            lst_logins.pop(indice)
            lst_senhas.pop(indice)
            break