# produto_service/database.py
class Database:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto['nome'] == nome:
                return produto
        return None

db = Database()
