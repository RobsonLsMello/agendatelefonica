from Model.DTO.PessoaDTO import PessoaDTO
from Model.DTO.ContatoDTO import ContatoDTO
import os

class PessoaView:
    def __init__(self):
        self.mensagem = ""

    def inicio(self, pessoa:PessoaDTO):
        os.system("cls")
        print("╔{}╗".format("═"*128))
        print("║{:<128}║".format(pessoa.nome))
        print("╠{}╦{}╦{}╣".format("═"*11, "═"*100, "═"*15))
        print("║{:^11}║{:<100}║{:^15}║".format("Código", "Contato", "Tipo do Contato"))
        print("╠{}╬{}╬{}╣".format("═"*11, "═"*100, "═"*15))
        for contato in pessoa.contatos:
            print("║{:^11}║{:<100}║{:^15}║".format(contato.codigo, contato.numero, contato.tipoContato.nome))
        print("╚{}╩{}╩{}╝".format("═"*11, "═"*100, "═"*15))
        print("\n\n")

    def menu(self):
        print("┌──────────────────────────┐")
        print("│Menu:                     │")
        print("├──────────────────────────┤")
        print("│1 - Adicionar contato     │")
        print("│2 - Alterar contato       │")
        print("│3 - Deletar contato       │")
        print("│4 - Alterar dados Pessoais│")
        print("│5 - Voltar para a agenda  │")
        print("└──────────────────────────┘")
        print("{}".format(self.mensagem))
        self.mensagem = ""
        opcao = input("*Opção: ")
        return opcao

    def procurarCodigo(self, isAlteracao:bool = True):
        if(isAlteracao):
            print("Digite o número do código do contato para fazer alteração")
        else:
            print("Digite o número do código do contato para deletar")
        print("{}".format(self.mensagem))
        codigo = input("Código: ")
        self.mensagem = ""
        return codigo

    def colocarMensagem(self, codigo:int):
        print("•")
        if codigo == 1:
            self.mensagem += "\n\t■ Digite uma opção númerica"
        elif codigo == 2:
            self.mensagem += "\n\t■ Opção inválida"
        elif codigo == 3:
            self.mensagem += "\n\t■ Código apenas pode ser númerico"
        elif codigo == 4:
            self.mensagem += "\n\t■ Código de contato inválido"
        elif codigo == 5:
            self.mensagem += "\n\t■ Opção não tem Caractere(s) Especial(is)"
        elif codigo == 6:
            self.mensagem += "\n\t■ Código não tem Caractere(s) Especial(is)"
        elif codigo == 7:
            self.mensagem += "\n\t■ Por favor, preencha o  campo"
        else:
            self.mensagem += "\n\t■ Erro não identificado" 
