class Produtor:
    def __init__(self, id, produto):
        self.id = id
        self.produto = produto

    def criar_produto(self, produto):
        if(produto == []):
            self.produto.append((self.id, 1))
        else:
            self.produto.append((self.id, (produto[-1][1]+1)))