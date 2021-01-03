#nome = input('Digite seu nome: ')
usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'jessica'
senha_bd = '12345'

"""if 'a' in nome:
    print("Existe a letra a no seu nome.")
"""
if usuario_bd == usuario and senha_bd == senha:
    print("Login efetuaado com sucesso!")
else:
    print("Usuário e/ou senha inválidos.")