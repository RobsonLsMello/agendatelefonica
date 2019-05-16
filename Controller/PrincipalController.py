from View.PrincipalView import PrincipalView
from Model.DTO.PessoaDTO import PessoaDTO
from Model.DAO.AgendaDAO import AgendaDAO
from Controller.AdicionarPessoasController import AdicionarPessoasController
class PrincipalController:
    def __init__(self):
        principal = PrincipalView()
        agenda = AgendaDAO()
        opcao = 0
        while 0 == 0 or opcao == 999:
            opcao = principal.menu(agenda.selecionaPessoa(""))
            if opcao == 1:
                adicionarPessoas = AdicionarPessoasController()
                agenda.criaPessoa(adicionarPessoas.pessoa)
            
        