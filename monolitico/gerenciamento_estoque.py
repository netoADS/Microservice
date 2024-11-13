# Classe Produto que define o modelo de um produto
class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"Nome: {self.nome}, Quantidade: {self.quantidade}, Preço: R${self.preco:.2f}"


# Classe Estoque que gerencia os produtos no estoque
class Estoque:
    def __init__(self):
        self.produtos = []

    # Adicionar um novo produto ao estoque
    def adicionar_produto(self, nome, quantidade, preco):
        produto = Produto(nome, quantidade, preco)
        self.produtos.append(produto)
        print(f"Produto '{nome}' adicionado com sucesso!")

    # Listar todos os produtos em estoque
    def listar_produtos(self):
        if not self.produtos:
            print("Estoque vazio.")
        else:
            for produto in self.produtos:
                print(produto)

    # Buscar um produto pelo nome
    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        print(f"Produto '{nome}' não encontrado.")
        return None

    # Atualizar a quantidade de um produto em estoque
    def atualizar_quantidade(self, nome, nova_quantidade):
        produto = self.buscar_produto(nome)
        if produto:
            produto.quantidade = nova_quantidade
            print(f"Quantidade do produto '{nome}' atualizada para {nova_quantidade}.")

    # Remover um produto do estoque
    def remover_produto(self, nome):
        produto = self.buscar_produto(nome)
        if produto:
            self.produtos.remove(produto)
            print(f"Produto '{nome}' removido com sucesso!")


# Função principal para interação com o usuário
def main():
    estoque = Estoque()

    while True:
        print("\nGerenciamento de Estoque")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Buscar Produto")
        print("4. Atualizar Quantidade")
        print("5. Remover Produto")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade do produto: "))
            preco = float(input("Preço do produto: "))
            estoque.adicionar_produto(nome, quantidade, preco)

        elif opcao == "2":
            print("\nProdutos em Estoque:")
            estoque.listar_produtos()

        elif opcao == "3":
            nome = input("Nome do produto a buscar: ")
            produto = estoque.buscar_produto(nome)
            if produto:
                print("Produto encontrado:", produto)

        elif opcao == "4":
            nome = input("Nome do produto para atualizar: ")
            nova_quantidade = int(input("Nova quantidade: "))
            estoque.atualizar_quantidade(nome, nova_quantidade)

        elif opcao == "5":
            nome = input("Nome do produto a remover: ")
            estoque.remover_produto(nome)

        elif opcao == "6":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
