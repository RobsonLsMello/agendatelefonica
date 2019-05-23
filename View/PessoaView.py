from Model.DTO.PessoaDTO import PessoaDTO
from Model.DTO.ContatoDTO import ContatoDTO
import os

class PessoaView:
    def __init__(self):
        self.mensagem = "*                                                              *"

    def inicio(self, pessoa:PessoaDTO):
        os.system("cls")
        print("*"*130)
        print("*{}{}*".format(pessoa.nome," "*(128 - len(pessoa.nome))))
        print("*{}*".format("-"*128))
        print("*Codigo{}|Contato{}|Tipo do Contato*".format(" "*5, " "*93))
        print("*{}*".format("_"*128))
        for contato in pessoa.contatos:
            print("*{}{}|{}{}|{}{}*".format(contato.codigo, " "*(11 - len(str(contato.codigo))), contato.numero, " "*(100 - len(str(contato.numero))), contato.tipoContato.nome," "*(15 - len(contato.tipoContato.nome))))
        print("*{}*".format("_"*128))
        print("\n\n")
        print("*--------------------------------------------------------------*")

    def menu(self):
        print("*Menu:                                                         *")
        print("*1 - Adicionar contato                                         *")
        print("*2 - Alterar contato                                           *")
        print("*3 - Deletar contato                                           *")
        print("*4 - Alterar dados Pessoais                                    *")
        print("*5 - Voltar para a agenda                                      *")
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
        if codigo == 1:
            self.mensagem += "\n\tDigite uma opção númerica"
        elif codigo == 2:
            self.mensagem += "\n\tOpção inválida"
        elif codigo == 3:
            self.mensagem += "\n\tCódigo apenas pode ser númerico"
        elif codigo == 4:
            self.mensagem += "\n\tCódigo de contato inválido"
        elif codigo == 5:
            self.mensagem += "\n\tOpção não tem Caractere(s) Especial(is)"
        elif codigo == 6:
            self.mensagem += "\n\tCódigo não tem Caractere(s) Especial(is)"
        elif codigo == 7:
            self.mensagem += "\n\tPor favor, preencha o  campo"
        else:
            self.mensagem += "\n\tErro não identificado" 
