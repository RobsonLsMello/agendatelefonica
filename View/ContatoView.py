from Model.DTO.ContatoDTO import ContatoDTO
from Model.DTO.TipoContatoDTO import TipoContatoDTO
from Model.DTO.PessoaDTO import PessoaDTO
import os

class ContatoView:
    def __init__(self):
        self.mensagem = ""

    def formulario(self, isCadastro:bool):
        os.system("cls")
        print("_______________________________________________")
        if(isCadastro):
            print("|Formulário de cadastro de um Contato:        |")
        else:
            print("|Formulário de Alteração de um Contato:       |")            
        print("|                                             |")
    

    def formularioTipoContato(self, tipos:list):
        print("|Selecione o tipo de contato:                 |")
        for tipo in  tipos:
            print("|{} - {} \t\t\t\t      |".format(tipo.codigo, tipo.nome))
        print(self.mensagem)
        opcao  = input("|Tipo: ")
        print("_______________________________________________")   
        self.mensagem = ""
        return opcao

    def formularioNumero(self, tipo:int):
        if int(tipo) == 0:
            print("|Digite um número de telefone                 |")
        elif int(tipo) == 1:
            print("|Digite um número de celular                  |")
        elif int(tipo) == 2:
            print("|Digite um email                              |")
        else:
            print("|Digite um dado de contato                    |")
        print(self.mensagem)
        nome = input("|Dado: ")
        print("_______________________________________________")   
        self.mensagem = ""     
        return nome

    def colocarMensagem(self, codigo:int):
        if codigo == 1:
            self.mensagem += "\n\tDigite uma opção númerica"
        elif codigo == 2:
            self.mensagem += "\n\tOpção inválida"
        elif codigo == 3:
            self.mensagem += "\n\tPor favor, preencha o  campo"
        elif codigo == 4:
            self.mensagem += "\n\tUm telefone é composto apenas por números"
        elif codigo == 5:
            self.mensagem += "\n\tUm telefone deve ter 8 digitos"
        elif codigo == 6:
            self.mensagem += "\n\tUm celular é composto apenas por números"
        elif codigo == 7:
            self.mensagem += "\n\tUm celular deve ter 9 digitos"
        elif codigo == 8:
            self.mensagem += "\n\tContato pode ter até 100 caracteres"
        elif codigo == 9:
            self.mensagem += "\n\tUm email precisa conter ao menos 1 \".com\""
        elif codigo == 10:
            self.mensagem += "\n\tUm email precisa conter ao menos 1 \"@\""
        else:
            self.mensagem += "\n\tErro não identificado" 