from Model import Usuario, Livro
class ControlLogin:
    def __init__(self):
        self.usuariosRegistrados = {"danielzinho124@gmail.com": "Daniel123"}

    def login(self):
        email = input("Email: ")
        senha = input("Senha: ")
        if email in self.usuariosRegistrados and self.usuariosRegistrados[email] == senha:
            print("Login realizado com sucesso!")
        else:
            print("Email ou senha incorretos.")

class ControlCadastro:
    def __init__(self):
        self.usuariosCadastrados = {}

    def cadastrar(self):
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        dataNascimento = input("Data de Nascimento: ")
        email = input("Email para cadastro: ")
        senha = input("Senha para cadastro: ")
        usuarioNovo = Usuario(nome, endereco, telefone, dataNascimento, email, senha)
        if email not in self.usuariosCadastrados:
            self.usuariosCadastrados[email] = usuarioNovo
            print("Cadastro realizado com sucesso!")
        else:
            print("Usuário já cadastrado.")

class ControlLivro:
    def __init__(self):
        self.livrosDisponiveis = [
            Livro(1, "Dom Quixote", "Miguel de Cervantes", 29.90, 10),
            Livro(2, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 19.99, 15),
            Livro(3, "Orgulho e Preconceito", "Jane Austen", 24.50, 8),
            Livro(4, "O Senhor dos Anéis", "J.R.R. Tolkien", 49.99, 20),
            Livro(5, "Cem Anos de Solidão", "Gabriel García Márquez", 35.80, 12),
            Livro(6, "1984", "George Orwell", 27.30, 7),
            Livro(7, "Crime e Castigo", "Fiódor Dostoiévski", 31.20, 9),
            Livro(8, "A Revolução dos Bichos", "George Orwell", 22.90, 11),
            Livro(9, "O Diário de Anne Frank", "Anne Frank", 18.75, 14),
            Livro(10, "As Crônicas de Nárnia", "C.S. Lewis", 45.60, 6),
        ]

    def mostrarLivros(self):
        print("\nLivros disponíveis:")
        for livro in self.livrosDisponiveis:
            print(f"Código: {livro.codigo}, Título: {livro.titulo}, Autor: {livro.autor}, Preço: R${livro.preco}, Quantidade: {livro.quantidade}")

    def escolherLivro(self):
        codigo = int(input("\nDigite o código do livro que deseja comprar: "))
        for livro in self.livrosDisponiveis:
            if livro.codigo == codigo:
                print(f"\nLivro escolhido: {livro.titulo}")
                break
        else:
            print("Livro não encontrado.")

    def efetuarCompra(self):
        codigo = int(input("\nDigite o código do livro que deseja comprar: "))
        for livro in self.livrosDisponiveis:
            if livro.codigo == codigo:
                quantidade = int(input("Digite a quantidade desejada: "))
                if quantidade <= livro.quantidade:
                    print("\nCompra realizada com sucesso!")
                    livro.quantidade -= quantidade
                else:
                    print("Quantidade indisponível.")
                break
        else:
            print("Livro não encontrado.")

class ControlReserva:
    def __init__(self, livrosDisponiveis):
        self.livrosDisponiveis = livrosDisponiveis

    def realizarReserva(self):
        codigo = int(input("\nDigite o código do livro que deseja reservar: "))
        for livro in self.livrosDisponiveis:
            if livro.codigo == codigo:
                print(f"\nReserva realizada para o livro: {livro.titulo}")
                break
        else:
            print("Livro não encontrado.")
