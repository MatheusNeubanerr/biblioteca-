
from Livro import Livro
from Biblioteca import Biblioteca


# Exemplo de uso:
biblioteca = Biblioteca()

while True:
    print("\n1. Cadastrar Livro")
    print("2. Consultar Livro por Título")
    print("3. Listar Livros por Autor")
    print("4. Listar Livros por Gênero")
    print("5. Listar Todos os Livros")
    print("6. Salvar Dados em Arquivo")
    print("7. Carregar Dados de Arquivo")
    print("8. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano de publicação do livro: "))
        genero = input("Digite o gênero do livro: ")

        novo_livro = Livro(titulo, autor, ano, genero)
        biblioteca.cadastrar_livro(novo_livro)
        print("Livro cadastrado com sucesso!")

    elif opcao == "2":
        titulo = input("Digite o título do livro: ")
        biblioteca.consultar_livro(titulo)

    elif opcao == "3":
        autor = input("Digite o nome do autor: ")
        biblioteca.listar_livros_por_autor(autor)

    elif opcao == "4":
        genero = input("Digite o gênero: ")
        biblioteca.listar_livros_por_genero(genero)

    elif opcao == "5":
        print("\nLista de Todos os Livros:")
        biblioteca.listar_todos_livros()

    elif opcao == "6":
        nome_arquivo = input("Digite o nome do arquivo para salvar os dados: ")
        biblioteca.salvar_dados(nome_arquivo)
        print("Dados salvos com sucesso!")

    elif opcao == "7":
        nome_arquivo = input("Digite o nome do arquivo para carregar os dados: ")
        biblioteca.carregar_dados(nome_arquivo)
        print("Dados carregados com sucesso!")

    elif opcao == "8":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
