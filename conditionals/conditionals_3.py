usuario = "admin"
senha = "1234"
usu = input('Digite o usuario:')
sen = input('Digite a senha:')
while usu != usuario or sen != senha:
    if usu != usuario:
        print('usuario incorreto')
        usu = input('Digite o usuario:')
    if sen != senha:
        print('senha incorreta')
        sen = input('Digite a senha:')
if usu == usuario and sen == senha:
    print('acesso liberado')
