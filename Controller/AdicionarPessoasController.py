from View.AdicionarPessoaView import AdicionarPessoaView
from Model.DTO.PessoaDTO import PessoaDTO
from Lib.TextoUtil import TextoUtil


class AdicionarPessoasController:
    def __init__(self, isCadastro:bool = True):
        self.continuarCadastroContatosPessoa = False
        tela = AdicionarPessoaView()
        nome = "1" #setar erro esperado
        hasCaracteresEspeciais = True
        hasCaracteresNumericos = True
        while(nome.isnumeric() == True or hasCaracteresEspeciais or hasCaracteresNumericos or nome == "" or len(nome) > 100):
            nome = tela.formulario(isCadastro)
            hasCaracteresEspeciais =  TextoUtil().verificarTextoComCaracteresEspeciais(nome)
            hasCaracteresNumericos =  TextoUtil().verificarTextoComNumeros(nome)
            if(nome.isnumeric() or hasCaracteresNumericos):
                tela.colocarMensagem(1)
            if(nome == ""):
                tela.colocarMensagem(2)
            if(len(nome) > 100):
                tela.colocarMensagem(3)            
            if(hasCaracteresEspeciais):
                tela.colocarMensagem(6)
        self.pessoa = PessoaDTO(0, nome, "")
        tela.aparecerObservacoes(1)
        opcao = "a"
        if(isCadastro):
            while(opcao.isalpha() or opcao == "" or (opcao.isnumeric() and (int(opcao) <0 or int(opcao) > 1))):
                opcao = tela.posFormulario()
                if(opcao.isalpha()):
                    tela.colocarMensagem(5)
                else:
                    if(int(opcao) == 0):
                        self.continuarCadastroContatosPessoa = True            
                if(opcao.isnumeric() and (int(opcao) <0 or int(opcao) > 1)):
                    tela.colocarMensagem(4)
            

