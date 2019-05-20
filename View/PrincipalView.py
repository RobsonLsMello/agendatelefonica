from Model.DTO.PessoaDTO import PessoaDTO
import os

class PrincipalView:
    def __init__(self):
        self.mensagem = ""
        
    def mostrarAgenda(self, agenda):
        os.system("cls")
        print("\t\tAgenda dos MONSTROS\n\n")        
        print("|Codigo\t|Nome\t\t|\n")
        for pessoa in agenda:
            print("|{}\t|{}\t\t|".format(pessoa.codigo, pessoa.nome))

    def menu(self):        
        opcao = -1
        print("Você deseja?\n1-Adicionar Pessoas\n2-Selecionar Pessoa\n3-Procurar Pessoa\n4-Deletar Pessoa\n5-Finalizar programa")
        while(opcao < 0 or opcao > 5):
            opcao = int(input("Opção: "))
            if opcao < 0 or opcao > 5:
                print("Opção inválida, por favor, digite novamente")
        return opcao
    
    def selecionarPessoaPorCodigo(self):
        print("Digite o código da pessoa que você quer acessar/modificar")
        print(self.mensagem)
        opcao = input("Código: ")
        self.mensagem = ""
        return opcao
    
    def selecionarPessoaPorNome(self):
        print("Digite um nome para pesquisa de Pessoa")
        print(self.mensagem)
        nome = input("Nome: ")
        self.mensagem = ""
        return nome
    
    def colocarMensagem(self, codigo:int):
        if codigo == 1:
            self.mensagem += "\nCódigo deve ser númerico\n"
        elif codigo == 2:
            self.mensagem += "\nEsse código não pertecem a pessoa alguma"
