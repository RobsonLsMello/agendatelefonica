from Model.DTO.PessoaDTO import PessoaDTO
from Model.DAO.AgendaDAO import AgendaDAO
from View.PessoaView import PessoaView
from Controller.AdicionarPessoasController import AdicionarPessoasController
from Controller.ContatoController import ContatoController
class PessoaController:
    def __init__(self):
        self.view = PessoaView()
        self.agenda = AgendaDAO()

    def index(self, pessoa:PessoaDTO, continuarCadastroContatosPessoa:bool):
        opcao = "a"
        sair = False
        while(sair == False):            
            while(opcao.isalpha() or (opcao.isnumeric() and (int(opcao) <0 or int(opcao) > 5))):
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
                        pass
                    elif int(opcao) == 3:
                        pass
                    elif int(opcao) == 4:
                        adicionarPessoa = AdicionarPessoasController(False)
                        self.pessoa.nome = adicionarPessoa.pessoa.nome
                        self.agenda.atualizarPessoa(self.pessoa)
                    else:                        
                        sair = True
                        
                if(opcao.isnumeric() and (int(opcao) <1 or int(opcao) > 4)):
                    self.view.colocarMensagem(2)
                
        