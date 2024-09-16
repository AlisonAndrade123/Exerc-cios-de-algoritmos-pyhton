class Fila:
    def __init__(self):
        """Inicializa uma nova fila vazia."""
        self.itens = []
    
    def enfileirar(self, item):
        """Adiciona um item ao final da fila."""
        self.itens.append(item)
    
    def desenfileirar(self):
        """Remove e retorna o item do início da fila. Se a fila estiver vazia, retorna None."""
        if not self.esta_vazia():
            return self.itens.pop(0)
        else:
            print("Erro: A fila está vazia.")
            return None
    
    def inicio(self):
        """Retorna o item do início da fila sem removê-lo. Se a fila estiver vazia, retorna None."""
        if not self.esta_vazia():
            return self.itens[0]
        else:
            print("Erro: A fila está vazia.")
            return None
    
    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.itens) == 0
    
    def tamanho(self):
        """Retorna o número de itens na fila."""
        return len(self.itens)
    
    def __str__(self):
        """Representação em string da fila."""
        return str(self.itens)

# Exemplo de uso da fila
if __name__ == "__main__":
    # Cria uma fila
    fila = Fila()
    
    # Adiciona itens
    fila.enfileirar(10)
    fila.enfileirar(20)
    fila.enfileirar(30)
    
    print("Fila após enfileirar 10, 20, 30:", fila)
    
    # Remove um item
    print("Item desenfileirado:", fila.desenfileirar())
    
    print("Fila após desenfileirar:", fila)
    
    # Verifica o início da fila
    print("Início da fila:", fila.inicio())
    
    # Verifica se a fila está vazia
    print("A fila está vazia?", fila.esta_vazia())
    
    # Tamanho da fila
    print("Tamanho da fila:", fila.tamanho())