def enviar_email_confirmacao(usuario):
    corpo = f"Olá {usuario['nome']}, sua conta foi criada com sucesso!"
    print(f"Enviando e-mail para {usuario['email']} com corpo:\n{corpo}")
