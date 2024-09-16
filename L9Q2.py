# Cremilda Chantilly é uma dentista e precisa  de ajuda para o gerenciamento de filas de atendimento. Desenvolva um programa que permita adicionar pacientes na fila e indique a vez do paciente a ser atendido. Minimamente, disponibilize as funcionalidades de adicionar paciente e remover paciente.

class Fila:
    def __init__(self):
        """Inicializa uma nova fila vazia."""
        self.itens = []
    
    def enfileirar(self, paciente):
        """Adiciona um paciente ao final da fila."""
        self.itens.append(paciente)
    
    def desenfileirar(self):
        """Remove e retorna o paciente do início da fila. Se a fila estiver vazia, retorna None."""
        if not self.esta_vazia():
            return self.itens.pop(0)
        else:
            print("Erro: A fila está vazia.")
            return None
    
    def inicio(self):
        """Retorna o paciente do início da fila sem removê-lo. Se a fila estiver vazia, retorna None."""
        if not self.esta_vazia():
            return self.itens[0]
        else:
            print("Erro: A fila está vazia.")
            return None
    
    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.itens) == 0
    
    def tamanho(self):
        """Retorna o número de pacientes na fila."""
        return len(self.itens)
    
    def __str__(self):
        """Representação em string da fila."""
        return str(self.itens)

# Programa Principal
if __name__ == "__main__":
    fila = Fila()
    
    print("Bem-vindo ao sistema de gerenciamento de filas de atendimento!")
    
    while True:
        print("\nEscolha uma operação:")
        print("1. Adicionar paciente")
        print("2. Atender paciente")
        print("3. Ver próximo paciente")
        print("4. Sair")
        
        opcao = input("Digite o número da operação desejada: ")
        
        if opcao == '1':
            paciente = input("Digite o nome do paciente a ser adicionado: ")
            fila.enfileirar(paciente)
            print(f"Paciente '{paciente}' adicionado à fila.")
        
        elif opcao == '2':
            paciente = fila.desenfileirar()
            if paciente:
                print(f"Paciente '{paciente}' foi atendido.")
        
        elif opcao == '3':
            paciente = fila.inicio()
            if paciente:
                print(f"Próximo paciente a ser atendido: {paciente}")
        
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
        
        # Exibe o estado atual da fila
        print("\nEstado atual da fila:", fila)