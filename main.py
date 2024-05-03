from Model import Usuario, Livro
from Control import ControlLogin, ControlCadastro, ControlLivro, ControlReserva

def main():
    controleLogin = ControlLogin()
    controleCadastro = ControlCadastro()
    controleLivro = ControlLivro()
    # Passando a lista de livros disponíveis para o construtor de ControlReserva
    controleReserva = ControlReserva(controleLivro.livrosDisponiveis)

    while True:
        print("\n1. Login")
        print("2. Cadastro")
        print("3. Escolher Livro")
        print("4. Efetuar Compra")
        print("5. Realizar Reserva")
        print("6. Sair")
        opcao = input("\nEscolha a opção: ")

        if opcao == '1':
            controleLogin.login()
        elif opcao == '2':
            controleCadastro.cadastrar()
        elif opcao == '3':
            controleLivro.mostrarLivros()
            controleLivro.escolherLivro()
        elif opcao == '4':
            controleLivro.mostrarLivros()
            controleLivro.efetuarCompra()
        elif opcao == '5':
            controleLivro.mostrarLivros()
            controleReserva.realizarReserva()
        elif opcao == '6':
            break

if __name__ == "__main__":
    main()
