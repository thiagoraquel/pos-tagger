def enviar_email(usuario, assunto, corpo):
    print(f"Enviando e-mail para {usuario['email']}")
    print(f"Assunto: {assunto}")
    print(f"Corpo:\n{corpo}")

def criar_email_confirmacao(usuario):
    assunto = "Confirmação de Cadastro"
    corpo = f"Olá {usuario['nome']}, sua conta foi criada com sucesso!"
    enviar_email(usuario, assunto, corpo)
