def cadastrar_usuario(usuario):
    Usuario.registrar(usuario) 
    print(f"Usuário {usuario['nome']} cadastrado com sucesso!")

# Exemplo de uso
usuario = {
    "nome": "Ana",
    "sobrenome": "Silva",
    "email": "ana@email.com",
    "senha": "123456",
    "idade": 30,
    "endereco": "Rua das Flores",
    "telefone": "99999-0000"
}

cadastrar_usuario(usuario)
