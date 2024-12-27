class Estoque:
    def __init__(self, id, estoque):
        self.id = id
        self.estoque = estoque

    def consome_estoque(self, consumidor):
        if(len(self.estoque) <= 0):
            print("Sem estoque")
        else:
            consumido = self.estoque.pop(-1)
            print(f"Consumidor {consumidor.id} recebe item {consumido}")
    
    def preenche_estoque(self, produtor):
        self.estoque.append(produtor.produto[-1])
        print(f"Produtor {produtor.id} armazena item {produtor.produto[-1]}")