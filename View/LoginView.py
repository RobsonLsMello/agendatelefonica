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

    def formularioEmail(self, mail:str = "", teveErro:bool = False):
        nome = ""
        if teveErro == False:
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
    def mensagemErroAoLogar(self):
        os.system("cls")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║Erro ao logar                                             ║")
        print(self.mensagem)
        print("║Se quiser desistir da operação digite 999 no email        ║")
        print("╚══════════════════════════════════════════════════════════╝\n")
        self.mensagem = ""  
        
    def mensagemSucesso(self):
        print("║Usuário Conectado, pronto para uso de email               ║")
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
            self.mensagem += "║\t ■ Por favor, preencha o campo                     ║"
        elif codigo == 8:
            self.mensagem += "║\t ■ Problemas de autenticação:                      ║\n"
            self.mensagem += "║\t ■ Usuário ou senha inválidos                      ║\n"
            self.mensagem += "║\t ■ Permissão para uso de app's de baixa segurança  ║\n"
            self.mensagem += "║\t ■ Acesse para corrigir:                           ║\n"
            self.mensagem += "║\t https://myaccount.google.com/lesssecureapps       ║"
        elif codigo == 9:
            self.mensagem += "║\t ■ Servidor de acesso SMTP desativado              ║"
        else:
            self.mensagem += "\n\t■ Erro não identificado"