"""
    Date: 18/nov/2017
    Created by @Wenderson Júnio
    Programa para criar o arquivo de login
"""
def make():
    try:
        with open('login_file', 'w') as login_file:
            login_file.write(input("Digite seu usuário: "))
            login_file.write(";")
            login_file.write(input("Digite sua senha: "))
            login_file.close()
            return True
    except IOError:
        return False