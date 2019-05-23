from Model.DTO.PessoaDTO import PessoaDTO
import os

class PrincipalView:
    def __init__(self):
        self.mensagem = ""
        
    def mostrarAgenda(self, agenda):
        os.system("cls")
        print("\t\tAgenda dos MONSTROS\n\n")        
        print("|Codigo     |Nome{}|".format(" "*96))
        print("{}".format("-"*(114)))
        for pessoa in agenda:
            print("|{}{}|{}{}|".format(pessoa.codigo," "*(11 - len(str(pessoa.codigo))), pessoa.nome," "*(100 - len(pessoa.nome))))

    def menu(self):        
        opcao = -1
        print("Você deseja?\n1-Adicionar Pessoas\n2-Selecionar Pessoa\n3-Procurar Pessoa\n4-Deletar Pessoa\n5-Finalizar programa")
        print(self.mensagem)
        self.mensagem = ""
        opcao = input("Opção: ")
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
    
    def nenhumContatoEncontrado(self, nome:str):
        print("Você usou o termo {}, que retornou nenhum resultado".format(nome))
        print("Retornando ao menu principal\n\n")
        input("Pressione a tecla \"Enter\" para continuar")

    def colocarMensagem(self, codigo:int):
        if codigo == 1:
            self.mensagem += "\n\tCódigo deve conter apenas números"
        elif codigo == 2:
            self.mensagem += "\n\tEsse código não pertecem a pessoa alguma"
        elif codigo == 3:
            self.mensagem += "\n\tDigite uma opção númerica"
        elif codigo == 4:
            self.mensagem += "\n\tOpção inválida"
        elif codigo == 5:
            self.mensagem += "\n\tOpção não tem Caractere(s) Especial(is)"
        elif codigo == 6:
            self.mensagem += "\n\tCódigo não tem Caractere(s) Especial(is)"
        elif codigo == 7:
            self.mensagem += "\n\tPor favor, preencha o  campo"
        else:
            self.mensagem += "\n\tErro não identificado"
