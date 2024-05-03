class Usuario:
    def __init__(self, nome, endereco, telefone, dataNascimento, email, senha):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.dataNascimento = dataNascimento
        self.email = email
        self.senha = senha

class Livro:
    def __init__(self, codigo, titulo, autor, preco, quantidade):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.quantidade = quantidade
