# estoque_service/database.py
class Database:
    def __init__(self):
        self.estoque = {}

    def atualizar_quantidade(self, nome, quantidade):
        if nome in self.estoque:
            self.estoque[nome] += quantidade
        else:
            self.estoque[nome] = quantidade

    def remover_produto(self, nome):
        if nome in self.estoque:
            del self.estoque[nome]

    def get_estoque(self):
        return self.estoque

db = Database()
