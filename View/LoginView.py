import os
from getpass import getpass

class LoginView:
    def __init__(self):
        self.mensagem = ""
    
    def index(self):
        os.system("cls")
        print("┌──────────────────────────────────────────────────────────────┐")
        print("│Você deseja entrar com um conta Gmail para poder enviar email?│")
        print("├──────────────────────────────────────────────────────────────┤")
        print("│1 - Sim                                                       │")
        print("│2 - Não                                                       │")
        print("│3 - Fechar a agenda                                           │")
        print("└──────────────────────────────────────────────────────────────┘")
        print("{}".format(self.mensagem))
        self.mensagem = ""
        opcao = input("*Opção: ")
        return opcao

    def formularioEmail(self, mail:str = ""):
        nome = ""
        os.system("cls")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║Digite seu endereço de email do Gmail                     ║")
        print("║Formato do email:                                         ║")
        print("║*ex: seuEmail@gmail.com                                   ║")
        if(mail == ""):
            if self.mensagem != "":
                print(self.mensagem)
            print("║                                                          ║")
            nome = input("║Gmail: ")
            self.mensagem = ""
        else:
            print("║Gmail: {:<51}║".format(mail))            
        print("╠══════════════════════════════════════════════════════════╣")   
         
        self.erro = 0   
        return nome

    def formularioSenha(self):
        senha = ""
        print("║Digite sua senha de email do Gmail                        ║")
        if self.mensagem != "":
            print(self.mensagem)
        print("║                                                          ║")
        senha = getpass("║Senha: ")
        print("╠══════════════════════════════════════════════════════════╣")   
        self.mensagem = ""  
        self.erro = 0   
        return senha

    def mensagemSucesso(self):
        print("║Usuário verificado, porém ainda não foi conectado         ║")
        print("╚══════════════════════════════════════════════════════════╝")
        os.system("Pause")   

    def colocarMensagem(self, codigo:int):
        print("•")
        if codigo == 1:
            self.mensagem += "\n\t■"
        elif codigo == 2:
            self.mensagem += "║\t■ Por favor, preencha o campo                      ║"
        elif codigo == 3:
            self.mensagem += "\n\t■ Digite uma opção númerica"
        elif codigo == 4:
            self.mensagem += "\n\t■ Opção inválida"
        elif codigo == 5:
            self.mensagem += "\n\t■ Opção não tem Caractere(s) Especial(is)"
        elif codigo == 6:
            self.mensagem += "\n\t■"
        elif codigo == 7:
            self.mensagem += "\t ■ Por favor, preencha o campo"
        else:
            self.mensagem += "\n\t■ Erro não identificado"