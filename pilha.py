class Pilha:
    def __init__(self):
        """Inicializa uma nova pilha vazia."""
        self.itens = []
    
    def empurrar(self, item):
        """Adiciona um item ao topo da pilha."""
        self.itens.append(item)
    
    def retirar(self):
        """Remove e retorna o item do topo da pilha. Se a pilha estiver vazia, retorna None."""
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            print("Erro: A pilha está vazia.")
            return None
    
    def topo(self):
        """Retorna o item do topo da pilha sem removê-lo. Se a pilha estiver vazia, retorna None."""
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            print("Erro: A pilha está vazia.")
            return None
    
    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.itens) == 0
    
    def tamanho(self):
        """Retorna o número de itens na pilha."""
        return len(self.itens)
    
    def __str__(self):
        """Representação em string da pilha."""
        return str(self.itens)

# Exemplo de uso da pilha
if __name__ == "__main__":
    # Cria uma pilha
    pilha = Pilha()
    
    # Adiciona itens
    pilha.empurrar(10)
    pilha.empurrar(20)
    pilha.empurrar(30)
    
    print("Pilha após empurrar 10, 20, 30:", pilha)
    
    # Retira um item
    print("Item retirado:", pilha.retirar())
    
    print("Pilha após retirar o topo:", pilha)
    
    # Verifica o topo da pilha
    print("Topo da pilha:", pilha.topo())
    
    # Verifica se a pilha está vazia
    print("A pilha está vazia?", pilha.esta_vazia())
    
    # Tamanho da pilha
    print("Tamanho da pilha:", pilha.tamanho())