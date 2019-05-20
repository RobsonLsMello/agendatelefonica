from View.PrincipalView import PrincipalView
from Model.DTO.PessoaDTO import PessoaDTO
from Model.DAO.AgendaDAO import AgendaDAO
from Controller.AdicionarPessoasController import AdicionarPessoasController
from Controller.PessoaController import PessoaController

class PrincipalController:
    def __init__(self):
        principal = PrincipalView()
        agenda = AgendaDAO()
        sair = False
        opcao = 0
        while sair == False:
            pessoas = agenda.selecionaPessoa("", False)
            principal.mostrarAgenda(pessoas)
            opcao = principal.menu()
            if opcao == 1:
                pessoaController = PessoaController()
                adicionarPessoas = AdicionarPessoasController()
                agenda.criaPessoa(adicionarPessoas.pessoa)      
                if adicionarPessoas.continuarCadastroContatosPessoa == True:      
                    pessoaController.index("" ,adicionarPessoas.continuarCadastroContatosPessoa)
            elif opcao == 2:
                self.procurarPessoasPorCodigo(pessoas, principal)
            elif opcao == 3:
                nome = principal.selecionarPessoaPorNome()
                pessoasPorNome = agenda.selecionaPessoa(nome, False)
                principal.mostrarAgenda(pessoasPorNome)
                self.procurarPessoasPorCodigo(pessoas, principal, False)
            elif opcao == 4:
                codigo = self.procurarPessoasPorCodigo(pessoas, principal, True, True)
                agenda.deletaPessoa(PessoaDTO(codigo, "",""))
            elif opcao == 5:
                sair = True
    
    def procurarPessoasPorCodigo(self, pessoas, principal, mostrarPessoas:bool = True, isDeletar:bool = False):
        codigo = "a"                
        naoTemPessoa = True
        while(codigo.isalpha() or naoTemPessoa):
            if(mostrarPessoas):
                principal.mostrarAgenda(pessoas)
            codigo = principal.selecionarPessoaPorCodigo()
            for pessoa in pessoas:
                if(int(codigo) == int(pessoa.codigo)):
                    naoTemPessoa = False
                    break
            if(codigo.isalpha()):
                principal.colocarMensagem(1)
            if(naoTemPessoa):
                principal.colocarMensagem(2)
        if(isDeletar == False):
            pessoaController = PessoaController()
            pessoaController.index(PessoaDTO(codigo,"", "") ,False)
        return codigo


                
            
        