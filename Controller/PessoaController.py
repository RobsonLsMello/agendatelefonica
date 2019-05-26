from Model.DTO.PessoaDTO import PessoaDTO
from Model.DTO.ContatoDTO import ContatoDTO
from Model.DAO.AgendaDAO import AgendaDAO
from View.PessoaView import PessoaView
from Controller.AdicionarPessoasController import AdicionarPessoasController
from Controller.ContatoController import ContatoController
from Lib.TextoUtil import TextoUtil
from Model.DTO.UsuarioDTO import UsuarioDTO
from Lib.EnviarEmail import EnviarEmail

class PessoaController:
    def __init__(self,usuario:UsuarioDTO = UsuarioDTO("","")):
        self.view = PessoaView(usuario)
        self.agenda = AgendaDAO()
        self.usuario = usuario

    def index(self, pessoa:PessoaDTO, continuarCadastroContatosPessoa:bool):        
        sair = False
        while(sair == False):    
            opcao = "a"   
            hasCaracteresEspeciais = True  
            hasCaracteresAlpha = True   
            while(opcao.isalpha() or opcao == "" or hasCaracteresEspeciais or hasCaracteresAlpha or (opcao.isnumeric() and (int(opcao) <1 or int(opcao) > 6))):
                if(continuarCadastroContatosPessoa):
                    self.pessoa = self.agenda.selecionaContato(self.agenda.selecionaPessoa("", True)[0])
                else:
                    self.pessoa = self.agenda.selecionaContato(self.agenda.selecionaPessoa("", False, pessoa.codigo)[0])
                self.view.inicio(self.pessoa)
                opcao = self.view.menu()
                hasCaracteresEspeciais = TextoUtil().verificarTextoComCaracteresEspeciais(opcao)
                hasCaracteresAlpha = TextoUtil().verificarTextoComAlpha(opcao)
                if(opcao == ""):
                    self.view.colocarMensagem(7)  
                else:
                    if(hasCaracteresEspeciais):
                        self.view.colocarMensagem(5)                
                    else:  
                        if(opcao.isalpha() or hasCaracteresAlpha):
                            self.view.colocarMensagem(1)
                        else:
                            if int(opcao) == 1:
                                contatoController = ContatoController()
                                contatoController.formulario(self.pessoa)
                            elif int(opcao) == 2:
                                codigo = self.validarCodigo()
                                contatoController = ContatoController()
                                contatoController.formulario(self.pessoa, False, codigo)
                            elif int(opcao) == 3:
                                codigo = self.validarCodigo(0)                    
                                self.agenda.deletaContato(ContatoDTO(codigo, "","","",""))
                            elif int(opcao) == 4:
                                adicionarPessoa = AdicionarPessoasController(False)
                                self.pessoa.nome = adicionarPessoa.pessoa.nome
                                self.agenda.atualizarPessoa(self.pessoa)
                            elif int(opcao) == 5:                       
                                sair = True
                            elif int(opcao) == 6:                       
                                if(self.usuario.logado):
                                    self.pessoa = self.agenda.selecionaContato(self.pessoa, 1)
                                    self.enviarEmail(self.validarCodigo(2))
                                    
                                else:
                                    self.view.erroEnviarEmail()                                   
                        if(opcao.isnumeric() and (int(opcao) <1 or int(opcao) > 6)):
                            self.view.colocarMensagem(2)
                
    def enviarEmail(self, codigo:int):
        novaPessoa = PessoaDTO(codigo, "", "")
        self.pessoa = self.agenda.selecionaContato(novaPessoa, 2)
        dados = self.view.formularioEmail(self.pessoa.contatos[0])
        try:
            envioDeEmail = EnviarEmail()
            envioDeEmail.setDadosDestinario(self.pessoa.contatos[0].numero, dados[0])
            envioDeEmail.setDadosRemetente(self.usuario)
            envioDeEmail.setMensagem(dados[1])
            envioDeEmail.enviarEmail()
            input("Enviado com Sucesso")
        except Exception:
            input("Falha no envio, favor verificar o email do destinatário")
        

    def validarCodigo(self, opcao:int = 1):
        codigo = "a"
        naoExisteContato = True
        hasCaracteresAlpha = True
        hasCaracteresEspeciais = True        
        while(codigo.isalpha() or codigo == "" or naoExisteContato or hasCaracteresAlpha or hasCaracteresEspeciais):
            self.view.inicio(self.pessoa)
            codigo = self.view.procurarCodigo(opcao)
            hasCaracteresEspeciais = TextoUtil().verificarTextoComCaracteresEspeciais(codigo)
            hasCaracteresAlpha = TextoUtil().verificarTextoComAlpha(codigo)
            if(codigo == ""):
                self.view.colocarMensagem(7)
            else:
                if(hasCaracteresEspeciais):
                    self.view.colocarMensagem(6)
                else:    
                    if(codigo.isalpha() or hasCaracteresAlpha):
                        self.view.colocarMensagem(3)
                    else:
                        for contato in self.pessoa.contatos:
                            if(int(codigo) == contato.codigo):
                                naoExisteContato = False
                                break
                    if(naoExisteContato):
                        self.view.colocarMensagem(4)
        return codigo
        