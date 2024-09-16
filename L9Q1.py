# Tuconaldo Tripa é mecânico e anda meio broco. Precisa de sua ajuda. Desenvolva um programa que receba os nomes das peças que ele está removendo, na ordem, e depois vá indicando, uma a uma,  na ordem inversa da adição, as peças para remontar o carro. Operações adicionar peça e remover peça.

class Pilha:
    def __init__(self):
        """Inicializa uma nova pilha vazia."""
        self.itens = []
    
    def empilhar(self, item):
        """Adiciona um item ao topo da pilha."""
        self.itens.append(item)
    
    def desempilhar(self):
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

# Programa Principal
if __name__ == "__main__":
    pilha = Pilha()
    
    print("Bem-vindo ao programa de gerenciamento de peças!")
    
    while True:
        print("\nEscolha uma operação:")
        print("1. Adicionar peça")
        print("2. Remover peça")
        print("3. Sair")
        
        opcao = input("Digite o número da operação desejada: ")
        
        if opcao == '1':
            peça = input("Digite o nome da peça a ser adicionada: ")
            pilha.empilhar(peça)
            print(f"Peça '{peça}' adicionada.")
        
        elif opcao == '2':
            peça = pilha.desempilhar()
            if peça:
                print(f"Peça '{peça}' removida.")
        
        elif opcao == '3':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
        
        # Exibe o estado atual da pilha
        print("\nEstado atual da pilha:", pilha)
