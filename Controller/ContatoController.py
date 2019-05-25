from Model.DTO.ContatoDTO import ContatoDTO
from Model.DTO.PessoaDTO import PessoaDTO
from View.ContatoView import ContatoView
from Model.DAO.AgendaDAO import AgendaDAO
from Lib.TextoUtil import TextoUtil
from Lib.Validador import Validador

class ContatoController:
    def __init__(self):
        self.contatoView = ContatoView()
        self.agenda = AgendaDAO()

    def formulario(self,pessoa:PessoaDTO, isCadastro:bool = True, codigo:int = -1):
        self.contato = ContatoDTO("0", "1", "b", "b", pessoa.codigo) #setar contato com o pior dado possivel para validação
        tipos = self.agenda.selecionaTiposContato()
        #primeiro pedir tipo do contato
        hasCaracteresEspeciais = True
        hasCaracteresAlpha = True
        while(self.contato.tipoContato.codigo.isalpha() or hasCaracteresEspeciais or hasCaracteresAlpha or self.contato.tipoContato.codigo == "" or (self.contato.tipoContato.codigo.isnumeric() and (int(self.contato.tipoContato.codigo) <0 or int(self.contato.tipoContato.codigo) > len(tipos) - 1))):
            self.contatoView.formulario(isCadastro)
            self.contato.tipoContato.codigo = self.contatoView.formularioTipoContato(tipos)
            hasCaracteresEspeciais = TextoUtil().verificarTextoComCaracteresEspeciais(self.contato.tipoContato.codigo)
            hasCaracteresAlpha = TextoUtil().verificarTextoComAlpha(self.contato.tipoContato.codigo) 
            if(self.contato.tipoContato.codigo == ""):
                self.contatoView.colocarMensagem(3)
            else:
                if(hasCaracteresEspeciais):
                    self.contatoView.colocarMensagem(11)
                else:
                    if(self.contato.tipoContato.codigo.isalpha() or hasCaracteresAlpha):
                        self.contatoView.colocarMensagem(1)
                    else:
                        if(int(self.contato.tipoContato.codigo) == 0):
                            self.continuarCadastroContatosPessoa = True            
                        if(self.contato.tipoContato.codigo.isnumeric() and (int(self.contato.tipoContato.codigo) <0 or int(self.contato.tipoContato.codigo) > len(tipos)-1)):
                            self.contatoView.colocarMensagem(2)
        erroDeFormato = True
        while(erroDeFormato or self.contato.numero == ""):
            self.contatoView.formulario(isCadastro)
            self.contato.numero = self.contatoView.formularioNumero(self.contato.tipoContato.codigo)
            erroDeFormato = False
            if(self.contato.numero == ""):
                self.contatoView.colocarMensagem(3)
            else:
                if(int(self.contato.tipoContato.codigo) == 0):
                    if(self.contato.numero.isalpha() or TextoUtil().verificarTextoComAlpha(self.contato.numero)):
                        self.contatoView.colocarMensagem(4)
                        erroDeFormato = True
                    if(len(self.contato.numero) != 10):
                        self.contatoView.colocarMensagem(5)
                        erroDeFormato = True
                    if(TextoUtil().verificarTextoComCaracteresEspeciais(self.contato.numero)):
                        self.contatoView.colocarMensagem(12)
                        erroDeFormato = True
                elif(int(self.contato.tipoContato.codigo) == 1):
                    if(self.contato.numero.isalpha() or TextoUtil().verificarTextoComAlpha(self.contato.numero)):
                        self.contatoView.colocarMensagem(6)
                        erroDeFormato = True
                    if(len(self.contato.numero) != 11):
                        self.contatoView.colocarMensagem(7)
                        erroDeFormato = True
                    if(TextoUtil().verificarTextoComCaracteresEspeciais(self.contato.numero)):
                        self.contatoView.colocarMensagem(13)
                        erroDeFormato = True
                elif(int(self.contato.tipoContato.codigo) == 2):
                    tuplaDeErro = Validador().validarEmail(self.contato.numero)
                    erroDeFormato = tuplaDeErro[0]
                    self.contatoView.mensagem += tuplaDeErro[1]
        self.contatoView.mensagemSucesso()
            
                            

        if(isCadastro):
            self.agenda.criaContato(self.contato)
        else:
            self.contato.codigo = codigo
            self.agenda.alteraContato(self.contato)


        
        