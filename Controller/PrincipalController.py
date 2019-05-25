from View.PrincipalView import PrincipalView
from Model.DTO.PessoaDTO import PessoaDTO
from Model.DAO.AgendaDAO import AgendaDAO
from Controller.AdicionarPessoasController import AdicionarPessoasController
from Controller.PessoaController import PessoaController
from Lib.TextoUtil import TextoUtil
from Model.DTO.UsuarioDTO import UsuarioDTO

class PrincipalController:
    def __init__(self, usuario:UsuarioDTO = UsuarioDTO("","")):
        principal = PrincipalView()
        agenda = AgendaDAO()
        sair = False
        while sair == False:
            opcao = "a"
            hasCaracteresEspeciais = True
            hasCaracteresAlpha = True
            while(opcao.isalpha() or opcao == "" or hasCaracteresEspeciais or hasCaracteresAlpha or (opcao.isnumeric() and (int(opcao) <1 or int(opcao) > 5))):
                pessoas = agenda.selecionaPessoa("", False)
                principal.mostrarAgenda(pessoas)
                opcao = principal.menu()
                hasCaracteresEspeciais = TextoUtil().verificarTextoComCaracteresEspeciais(opcao)
                hasCaracteresAlpha = TextoUtil().verificarTextoComAlpha(opcao)
                if (opcao == ""):
                    principal.colocarMensagem(7)
                else:
                    if(hasCaracteresAlpha):
                        principal.colocarMensagem(3)
                    else:
                        if(hasCaracteresEspeciais):
                            principal.colocarMensagem(5)                
                        else:
                            if(opcao.isnumeric() and (int(opcao) <1 or int(opcao) > 5)):
                                principal.colocarMensagem(4)
                            if(opcao.isalpha()):
                                principal.colocarMensagem(3)
                            else:
                                if int(opcao) == 1:
                                    pessoaController = PessoaController()
                                    adicionarPessoas = AdicionarPessoasController()
                                    agenda.criaPessoa(adicionarPessoas.pessoa)      
                                    if adicionarPessoas.continuarCadastroContatosPessoa == True:      
                                        pessoaController.index("" ,adicionarPessoas.continuarCadastroContatosPessoa)
                                elif int(opcao) == 2:
                                    self.procurarPessoasPorCodigo(pessoas, principal)
                                elif int(opcao) == 3:
                                    principal.mostrarAgenda(pessoas)
                                    nome = principal.selecionarPessoaPorNome()
                                    pessoasPorNome = agenda.selecionaPessoa(nome, False)
                                    if(len(pessoasPorNome) > 0):
                                        principal.mostrarAgenda(pessoasPorNome)
                                        self.procurarPessoasPorCodigo(pessoas, principal, True)
                                    else:
                                        principal.nenhumContatoEncontrado(nome)
                                elif int(opcao) == 4:
                                    codigo = self.procurarPessoasPorCodigo(pessoas, principal, True, True)
                                    agenda.deletaPessoa(PessoaDTO(codigo, "",""))
                                elif int(opcao) == 5:
                                    sair = True
                            
    
    def procurarPessoasPorCodigo(self, pessoas, principal, mostrarPessoas:bool = True, isDeletar:bool = False):
        codigo = "a"                
        naoTemPessoa = True
        hasCaracteresEspeciais = True
        hasCaracteresAlpha = True
        while(codigo.isalpha() or codigo == "" or hasCaracteresEspeciais or hasCaracteresAlpha or naoTemPessoa):           
            if(mostrarPessoas):
                principal.mostrarAgenda(pessoas)
            codigo = principal.selecionarPessoaPorCodigo()   
            hasCaracteresEspeciais = TextoUtil().verificarTextoComCaracteresEspeciais(codigo)
            hasCaracteresAlpha = TextoUtil().verificarTextoComAlpha(codigo) 
            if(codigo == ""):
                principal.colocarMensagem(7)
            else:
                if(hasCaracteresEspeciais):
                    principal.colocarMensagem(6)
                else:        
                    if(codigo.isalpha() or hasCaracteresAlpha):
                        principal.colocarMensagem(1)
                    else:
                        for pessoa in pessoas:
                            if(int(codigo) == int(pessoa.codigo)):
                                naoTemPessoa = False
                                break
                    if(naoTemPessoa):
                        principal.colocarMensagem(2)
        if(isDeletar == False):
            pessoaController = PessoaController()
            pessoaController.index(PessoaDTO(codigo,"", "") ,False)
        return codigo


                
            
        