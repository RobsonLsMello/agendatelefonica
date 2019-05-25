from View.LoginView import LoginView
from Lib.TextoUtil import TextoUtil
from Lib.Validador import Validador
from Model.DTO.UsuarioDTO import UsuarioDTO
from Controller.PrincipalController import PrincipalController

class LoginController:
    def __init__(self):
        self.loginView = LoginView()
        self.usuarioDTO = UsuarioDTO("","")

    def index(self):   
        sair = False     
        while sair == False:
            opcao = "a"
            hasCaracteresEspeciais = True
            hasCaracteresAlpha = True
            while(opcao.isalpha() or opcao == "" or hasCaracteresEspeciais or hasCaracteresAlpha or (opcao.isnumeric() and (int(opcao) <1 or int(opcao) > 3))):
                opcao = self.loginView.index()
                hasCaracteresEspeciais = TextoUtil().verificarTextoComCaracteresEspeciais(opcao)
                hasCaracteresAlpha = TextoUtil().verificarTextoComAlpha(opcao)
                if (opcao == ""):
                    self.loginView.colocarMensagem(7)
                else:
                    if(hasCaracteresAlpha):
                        self.loginView.colocarMensagem(3)
                    else:
                        if(hasCaracteresEspeciais):
                            self.loginView.colocarMensagem(5)                
                        else:
                            if(opcao.isnumeric() and (int(opcao) <1 or int(opcao) > 3)):
                                self.loginView.colocarMensagem(4)
                            if(opcao.isalpha()):
                                self.loginView.colocarMensagem(3)
                            else:
                                if(int(opcao) == 1):
                                    self.acessarContaGmail()
                                elif(int(opcao) == 3):
                                    sair == True
            if(sair == False):
                principal = PrincipalController(self.usuarioDTO)

    def acessarContaGmail(self):
        erroDeFormato = True
        email = ""
        senha = ""
        while(erroDeFormato or email == ""):
            email = self.loginView.formularioEmail()            
            if(email == ""):
                self.loginView.colocarMensagem(7)
            else:
                tuplaDeErro = Validador().validarEmail(email)
                erroDeFormato = tuplaDeErro[0]
                self.loginView.mensagem += tuplaDeErro[1]
        while(senha == ""):
            self.loginView.formularioEmail(email)
            senha = self.loginView.formularioSenha()
            if(senha == ""):
                self.loginView.colocarMensagem(2)