import os

class AdicionarPessoaView:
    def __init__(self):        
        self.mensagem = "|\t\t\t\t\t      |"

    def formulario(self, isCadastro:bool = True):
        os.system("cls")
        print("_______________________________________________")
        if(isCadastro):
            print("|Formulário de cadastro de uma Pessoa:        |")
        else:
            print("|Formulário de Alteração de uma Pessoa:       |")            
        print("|                                             |")
        print("|Digite um nome                               |")
        print(self.mensagem)
        nome = input("|Nome: ")
        print("_______________________________________________")   
        self.mensagem = ""     
        return nome

    def posFormulario(self):
        print("\n\n")
        print(self.mensagem)
        print("Deseja cadastrar números ou emails para esta pessoa?\nSelecione:\n0 - Para Continuar\n1 - Para Voltar para a Agenda")
        return input("Opção: ")
    
    def colocarMensagem(self, codigoErro:int):
        if codigoErro == 1:
            self.mensagem += "|Nome não pode ter números            |\n"
        elif codigoErro  == 2:
            self.mensagem += "|Nome não pode estar vázio            |\n"
        elif codigoErro  == 3:
            self.mensagem += "|Nome com mais de 100(cem) caracteres |\n"
        elif codigoErro == 4:
            self.mensagem = "Opção deve estar entre os números 0 e 1\n"
        elif codigoErro == 5:
            self.mensagem = "Opção deve ser um número\n"
        else:
            self.mensagem += "|Erro não esperado                    |\n"

    def aparecerObservacoes(self, codigo:int):
        if codigo == 1:
            print("Pessoa adicionada com sucesso!\n\n")
        elif codigo == 2:
            print("")
