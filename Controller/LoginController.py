from View.LoginView import LoginView
from Lib.TextoUtil import TextoUtil
from Lib.Validador import Validador
from Lib.EnviarEmail import EnviarEmail
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
                pass

    def acessarContaGmail(self):
        sair = False
        teveErro = False
        while(sair == False):            
            erroDeFormato = True
            email = ""
            senha = ""
            if(teveErro):
                self.loginView.mensagemErroAoLogar()
            while(erroDeFormato or email == ""):
                email = self.loginView.formularioEmail("", teveErro)  
                teveErro = True 
                if(email == "999"):
                    break         
                if(email == ""): 
                    self.loginView.colocarMensagem(7)
                else:
                    tuplaDeErro = Validador().validarEmail(email)
                    erroDeFormato = tuplaDeErro[0]
                    self.loginView.mensagem += tuplaDeErro[1]
            if(email == "999"):
                break
            while(senha == ""):
                self.loginView.formularioEmail(email)
                senha = self.loginView.formularioSenha()
                if(senha == ""):
                    self.loginView.colocarMensagem(2)
            self.usuarioDTO.email = email
            self.usuarioDTO.senha = senha
            enviarEmail = EnviarEmail()
            enviarEmail.setDadosRemetente(UsuarioDTO(self.usuarioDTO.email, self.usuarioDTO.senha))
            enviarEmail.setDadosDestinario("python.agenda@gmail.com", "Teste de Login")
            enviarEmail.setMensagem("Teste de Login")
            if(enviarEmail.enviarEmail() == 0):
                self.loginView.mensagemSucesso()
                self.usuarioDTO.logado = True
                sair = True                
            elif (enviarEmail.enviarEmail() == 1):
                self.loginView.colocarMensagem(8)
                teveErro = True
            elif (enviarEmail.enviarEmail() == 2):
                self.loginView.colocarMensagem(9)
                teveErro = True
            else:
                self.loginView.colocarMensagem(999)
                teveErro = True
        
        