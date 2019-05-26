from Model.DTO.PessoaDTO import PessoaDTO
from Model.DTO.UsuarioDTO import UsuarioDTO
import os

class PrincipalView:
    def __init__(self, usuario:UsuarioDTO = UsuarioDTO("","")):
        self.mensagem = ""
        self.usuario = usuario
        
    def mostrarAgenda(self, agenda):
        os.system("cls")
        print("\t\tAgenda dos MONSTROS\n\n")
        arrayLogin = []
        arrayLogin.append("┌{}┐".format("─"*len(self.usuario.email)))
        arrayLogin.append("│{}{}│".format("Gmail Conectado:"," "*(len(self.usuario.email) - 16)))
        arrayLogin.append("├{}┤".format("─"*len(self.usuario.email)))
        arrayLogin.append("│{}│".format(self.usuario.email))
        arrayLogin.append("└{}┘".format("─"*len(self.usuario.email)))
        if(len(agenda) < 2 or self.usuario.logado == False):
            if(self.usuario.logado):    
                for itemLogin in arrayLogin:
                    print(itemLogin)
            print("╔{}╦{}╗".format("═"*(11), "═"*(100)))  
            print("║{:^11}║{:<100}║".format("Código", "Nome"))
            print("╠{}╬{}╣".format("═"*(11), "═"*(100)))   
        else:                   
            print("╔{}╦{}╗  {}".format("═"*(11), "═"*(100), arrayLogin[0]))  
            print("║{:^11}║{:<100}║  {}".format("Código", "Nome", arrayLogin[1]))
            print("╠{}╬{}╣  {}".format("═"*(11), "═"*(100), arrayLogin[2]))        
        for indice, pessoa in enumerate(agenda):
            if(indice <2 and self.usuario.logado):
                print("║{:^11}║{:<100}║  {}".format(pessoa.codigo, pessoa.nome, arrayLogin[3 + indice]))
            else:
                print("║{:^11}║{:<100}║".format(pessoa.codigo, pessoa.nome))
        print("╚{}╩{}╝".format("═"*(11), "═"*(100))) 
        print("\n\n") 

    def menu(self):        
        opcao = -1
        print(  "┌────────────────────────┐")
        print(  "│Você deseja?            │\n"+
                "├────────────────────────┤\n"
                "│1-Adicionar Pessoas     │\n"+
                "│2-Selecionar Pessoa     │\n"+
                "│3-Procurar Pessoa       │\n"+
                "│4-Deletar Pessoa        │\n"+
                "│5-Voltar                │")
        print(  "└────────────────────────┘")
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
        print("•")
        if codigo == 1:
            self.mensagem += "\n\t■ Código deve conter apenas números"
        elif codigo == 2:
            self.mensagem += "\n\t■ Esse código não pertecem a pessoa alguma"
        elif codigo == 3:
            self.mensagem += "\n\t■ Digite uma opção númerica"
        elif codigo == 4:
            self.mensagem += "\n\t■ Opção inválida"
        elif codigo == 5:
            self.mensagem += "\n\t■ Opção não tem Caractere(s) Especial(is)"
        elif codigo == 6:
            self.mensagem += "\n\t■ Código não tem Caractere(s) Especial(is)"
        elif codigo == 7:
            self.mensagem += "\n\t■ Por favor, preencha o  campo"
        else:
            self.mensagem += "\n\t■ Erro não identificado"
