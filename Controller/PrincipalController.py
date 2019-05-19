from View.PrincipalView import PrincipalView
from Model.DTO.PessoaDTO import PessoaDTO
from Model.DAO.AgendaDAO import AgendaDAO
from Controller.AdicionarPessoasController import AdicionarPessoasController
from Controller.PessoaController import PessoaController

class PrincipalController:
    def __init__(self):
        principal = PrincipalView()
        agenda = AgendaDAO()
        pessoaController = PessoaController()
        opcao = 0
        while 0 == 0 or opcao == 999:
            opcao = principal.menu(agenda.selecionaPessoa("", False))
            if opcao == 1:
                adicionarPessoas = AdicionarPessoasController()
                agenda.criaPessoa(adicionarPessoas.pessoa)      
                if adicionarPessoas.continuarCadastroContatosPessoa == True:      
                    pessoaController.index("" ,adicionarPessoas.continuarCadastroContatosPessoa)
            elif opcao ==2:
                pessoaController.index(PessoaDTO(0,"", "") ,False)

                
            
        