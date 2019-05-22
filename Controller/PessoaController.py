from Model.DTO.PessoaDTO import PessoaDTO
from Model.DTO.ContatoDTO import ContatoDTO
from Model.DAO.AgendaDAO import AgendaDAO
from View.PessoaView import PessoaView
from Controller.AdicionarPessoasController import AdicionarPessoasController
from Controller.ContatoController import ContatoController
class PessoaController:
    def __init__(self):
        self.view = PessoaView()
        self.agenda = AgendaDAO()

    def index(self, pessoa:PessoaDTO, continuarCadastroContatosPessoa:bool):        
        sair = False
        while(sair == False):    
            opcao = "a"        
            while(opcao.isalpha() or (opcao.isnumeric() and (int(opcao) <1 or int(opcao) > 5))):
                if(continuarCadastroContatosPessoa):
                    self.pessoa = self.agenda.selecionaContato(self.agenda.selecionaPessoa("", True)[0])
                else:
                    self.pessoa = self.agenda.selecionaContato(self.agenda.selecionaPessoa("", False, pessoa.codigo)[0])
                self.view.inicio(self.pessoa)
                opcao = self.view.menu()  
                if(opcao.isalpha()):
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
                        codigo = self.validarCodigo(False)                    
                        self.agenda.deletaContato(ContatoDTO(codigo, "","","",""))
                    elif int(opcao) == 4:
                        adicionarPessoa = AdicionarPessoasController(False)
                        self.pessoa.nome = adicionarPessoa.pessoa.nome
                        self.agenda.atualizarPessoa(self.pessoa)
                    elif int(opcao) == 5:                       
                        sair = True                                      
                if(opcao.isnumeric() and (int(opcao) <1 or int(opcao) > 4)):
                    self.view.colocarMensagem(2)
                
    
    def validarCodigo(self, isAlteracao:bool = True):
        codigo = "a"
        naoExisteContato = True
        while(codigo.isalpha() or naoExisteContato):
            codigo = self.view.procurarCodigo(isAlteracao)
            if(codigo.isalpha()):
                self.view.colocarMensagem(3)
            for contato in self.pessoa.contatos:
                if(int(codigo) == contato.codigo):
                    naoExisteContato = False
                    break
            if(naoExisteContato):
                self.view.colocarMensagem(4)
        return codigo
        