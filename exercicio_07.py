import psycopg

print(psycopg)

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

# definição do método: ele recebe um objeto do tipo Usuario
def existe(usuario):
    # Abre a conexão
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20221_pessoal_db_login",
        user="postgres",
        password="postgres"
    ) as conexao:
        # obtém um cursor
        with conexao.cursor() as cursor:
            # executa o comando
            cursor.execute('SELECT * FROM tb_usuario WHERE login=%s AND senha=%s', 
                           (f'{usuario.login}', f'{usuario.senha}'))
            # obtém o resultado
            result = cursor.fetchone()
            # verifica se o resultado é diferente de None, o que indica que o usuário existe na base
            return result is not None

# definição da função menu
def menu():
    # texto a ser exibido
    texto = "0-Fechar Sistema\n1-Login\n2-Logoff\n"
    # usuário ainda não existe
    usuario = None
    # capturamos a opção do usuário
    op = int(input(texto))
    
    # enquanto ele não digitar zero
    while op != 0:
        # se digitar 1, capturamos login e senha e verificamos se o usuário existe na base
        if op == 1:
            login = input("Digite seu login\n")
            senha = input("Digite sua senha\n")
            usuario = Usuario(login, senha)
            print("Usuário OK!!!" if existe(usuario) else "Usuário NOK!!!")
        # se ele digitar 2, configuramos o usuario como "None" novamente
        elif op == 2:
            usuario = None
            print("Logoff realizado com sucesso")
        
        op = int(input(texto))
    
    # se digitar zero, dizemos adeus
    print("Até mais")

# chamamos a função menu
menu()
