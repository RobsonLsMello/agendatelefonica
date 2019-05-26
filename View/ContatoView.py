from Model.DTO.ContatoDTO import ContatoDTO
from Model.DTO.TipoContatoDTO import TipoContatoDTO
from Model.DTO.PessoaDTO import PessoaDTO
import os

class ContatoView:
    def __init__(self):
        self.mensagem = ""
        self.erros = 0

    def formulario(self, isCadastro:bool):
        os.system("cls")
        print("╔══════════════════════════════════════════════════════════╗")
        if(isCadastro):
            print("║Formulário de cadastro de um Contato:                     ║")
        else:
            print("║Formulário de Alteração de um Contato:                    ║")            
        print("║                                                          ║")
    

    def formularioTipoContato(self, tipos:list):
        print("║Selecione o tipo de contato:                              ║")
        for tipo in  tipos:
            print("║{} - {} \t\t\t\t                   ║".format(tipo.codigo, tipo.nome))
        if self.mensagem != "":
            print(self.mensagem)        
        opcao  = input("║Tipo: ")        
        print("╠══════════════════════════════════════════════════════════╣")  
        self.mensagem = ""     
        self.erro = 0 
        return opcao

    def formularioNumero(self, tipo:int):
        if int(tipo) == 0:
            print("║Digite um número de telefone                              ║")
            print("║Formato do telefone:                                      ║")
            print("║*Sem DDI                                                  ║")
            print("║*Com 10 digitos, ex: 1330302041                           ║")

        elif int(tipo) == 1:
            print("║Digite um número de celular                               ║")
            print("║Formato do celular:                                       ║")
            print("║*Sem DDI                                                  ║")
            print("║*Com 11 digitos, ex: 13996202020                          ║")
        elif int(tipo) == 2:
            print("║Digite um endereço de email                               ║")
            print("║Formato do email:                                         ║")
            print("║*Com até 100 caracteres                                   ║")
            print("║*ex: seuEmail@dominio.com                                 ║")
        else:
            print("║Digite um dado de contato                                 ║")
        if self.mensagem != "":
            print(self.mensagem)
        print("║                                                          ║")
        nome = input("║Dado: ")
        print("╠══════════════════════════════════════════════════════════╣")   
        self.mensagem = ""  
        self.erro = 0   
        return nome
    
    def mensagemSucesso(self):
        print("║Contato cadastrado com sucesso!                           ║")
        print("╚══════════════════════════════════════════════════════════╝")
        os.system("Pause")   
        

    def colocarMensagem(self, codigo:int):
        if self.erro != 0:
            self.mensagem += "\n"
        else:
            self.mensagem += "║\t                                                   ║\n"
        if codigo == 1:
            self.mensagem += "║\t■ Digite uma opção númerica                        ║"            
        elif codigo == 2:
            self.mensagem += "║\t■ Opção inválida                                   ║"
        elif codigo == 3:
            self.mensagem += "║\t■ Por favor, preencha o campo                      ║"
        elif codigo == 4:
            self.mensagem += "║\t■ Um telefone é composto apenas por números        ║"
        elif codigo == 5:
            self.mensagem += "║\t■ Um telefone deve ter 10(dez) digitos             ║"
        elif codigo == 6:
            self.mensagem += "║\t■ tUm celular é composto apenas por números        ║"
        elif codigo == 7:
            self.mensagem += "║\t■ Um celular deve ter 11(onze) digitos             ║"
        
        else:
            self.mensagem += "║\t■ Erro não identificado                            ║" 
        self.erro = self.erro + 1