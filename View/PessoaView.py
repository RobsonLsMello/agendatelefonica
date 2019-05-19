from Model.DTO.PessoaDTO import PessoaDTO
from Model.DTO.ContatoDTO import ContatoDTO
import os

class PessoaView:
    def __init__(self):
        self.mensagem = "*                                                              *"

    def inicio(self, pessoa:PessoaDTO):
        os.system("cls")
        print("****************************************************************")
        print("*{}\t\t\t\t\t\t\t*".format(pessoa.nome))
        print("*--------------------------------------------------------------*")
        print("*Codigo\t|Contato\t\t| Tipo do Contato\t      *")
        for contato in pessoa.contatos:
            print("*{}\t|{}\t\t|{}\t*".format(contato.codigo, contato.numero, contato.tipoContato.nome))
        print("*                                                              *")
        print("*                                                              *")

    def menu(self):
        print("*Menu:                                                         *")
        print("*1 - Adicionar contato                                         *")
        print("*2 - Alterar contato                                           *")
        print("*3 - Deletar contato                                           *")
        print("*4 - Alterar dados Pessoais                                    *")
        print("*5 - Voltar para a agenda                                    *")
        print("{}".format(self.mensagem))
        self.mensagem = ""
        opcao = input("*Opção: ")
        return opcao

    def colocarMensagem(self, codigo:int):
        if codigo == 1:
            self.mensagem += "\n\tDigite uma opção númerica"
        elif codigo == 2:
            self.mensagem += "\n\tOpção inválida"
        else:
            self.mensagem += "\n\tErro não identificado" 
