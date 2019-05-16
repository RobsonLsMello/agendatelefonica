from View.AdicionarPessoaView import AdicionarPessoaView
from Model.DTO.PessoaDTO import PessoaDTO

class AdicionarPessoasController:
    def __init__(self):
        tela = AdicionarPessoaView()
        nome = "1" #setar erro esperado
        while(nome.isalpha() == False or nome == "" or len(nome) > 100):
            nome = tela.formulario()
            if(nome.isalpha() == False):
                tela.colocarMensagem(1)
            if(nome == ""):
                tela.colocarMensagem(2)
            if(len(nome) > 100):
                tela.colocarMensagem(3)
        self.pessoa = PessoaDTO(0, nome, "")
        tela.aparecerObservacoes(1)
        opcao = "a"
        while(opcao.isalpha() or (opcao.isnumeric() and (int(opcao) <0 or int(opcao) > 1))):
            opcao = tela.posFormulario()
            if(opcao.isalpha()):
                tela.colocarMensagem(5)
            if(opcao.isnumeric() and (int(opcao) <0 or int(opcao) > 1)):
                tela.colocarMensagem(4)

