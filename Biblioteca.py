import pickle

class Biblioteca:

    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def consultar_livro(self, titulo):
        if titulo in self.livros:
            livro = self.livros[titulo]
            print(f'Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Gênero: {livro.genero}')
        else:
            print('Livro não encontrado.')

    def listar_livros_por_autor(self, autor):
        livros_autor = [livro for livro in self.livros.values() if livro.autor == autor]
        if livros_autor:
            for livro in livros_autor:
                print(f'Título: {livro.titulo}, Ano: {livro.ano}, Gênero: {livro.genero}')
        else:
            print('Nenhum livro encontrado para esse autor.')

    def listar_livros_por_genero(self, genero):
        livros_genero = [livro for livro in self.livros.values() if livro.genero == genero]
        if livros_genero:
            for livro in livros_genero:
                print(f'Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}')
        else:
            print('Nenhum livro encontrado para esse gênero.')

    def listar_todos_livros(self):
        if self.livros:
            for livro in self.livros.values():
                print(f'Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Gênero: {livro.genero}')
        else:
            print('Biblioteca vazia.')

    def salvar_dados(self, nome_arquivo):
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.livros, arquivo)

    def carregar_dados(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                self.livros = pickle.load(arquivo)
        except FileNotFoundError:
            print('Arquivo não encontrado.')

            