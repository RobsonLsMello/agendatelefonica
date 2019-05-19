from Model.DTO.PessoaDTO import PessoaDTO
from Model.DAO.AgendaDAO import AgendaDAO
from View.PessoaView import PessoaView

class PessoaController:
    def __init__(self):
        self.view = PessoaView()
        self.agenda = AgendaDAO()

    def index(self, pessoa:PessoaDTO, continuarCadastroContatosPessoa:bool):
        opcao = "a"
        while(0 == 0 or opcao == 999):
            if(continuarCadastroContatosPessoa):
                self.pessoa = self.agenda.selecionaContato(self.agenda.selecionaPessoa("", True)[0])
            else:
                self.pessoa = self.agenda.selecionaContato(self.agenda.selecionaPessoa("", False, pessoa.codigo)[0])
            print("\n\n\n")
            self.view.inicio(self.pessoa)    
            while(opcao.isalpha() or (opcao.isnumeric() and (int(opcao) <0 or int(opcao) > 3 or int(opcao) != 999))):
                opcao = self.view.menu()  
                if(opcao.isalpha()):
                    self.view.colocarMensagem(1)
                else:
                    if opcao == 0:
                        pass
                    elif opcao == 1:
                        pass
                    elif opcao == 2:
                        pass
                    elif opcao == 3:
                        pass
                if(opcao.isnumeric() and (int(opcao) <0 or int(opcao) > 1)):
                    self.view.colocarMensagem(2)
                
        