from Model.DTO.PessoaDTO import PessoaDTO
from Model.DTO.ContatoDTO import ContatoDTO
import os
from Model.DTO.UsuarioDTO import UsuarioDTO

class PessoaView:
    def __init__(self,usuario:UsuarioDTO = UsuarioDTO("","")):
        self.mensagem = ""
        self.usuario = usuario

    def inicio(self, pessoa:PessoaDTO):
        os.system("cls")
        print("╔{}╗".format("═"*128))
        print("║{:<128}║".format(pessoa.nome))
        print("╠{}╦{}╦{}╣".format("═"*11, "═"*100, "═"*15))
        print("║{:^11}║{:<100}║{:^15}║".format("Código", "Contato", "Tipo do Contato"))
        print("╠{}╬{}╬{}╣".format("═"*11, "═"*100, "═"*15))
        for contato in pessoa.contatos:
            print("║{:^11}║{:<100}║{:^15}║".format(contato.codigo, contato.numero, contato.tipoContato.nome))
        print("╚{}╩{}╩{}╝".format("═"*11, "═"*100, "═"*15))
        print("\n\n")

    def menu(self):
        print("┌──────────────────────────┐")
        print("│Menu:                     │")
        print("├──────────────────────────┤")
        print("│1 - Adicionar contato     │")
        print("│2 - Alterar contato       │")
        print("│3 - Deletar contato       │")
        print("│4 - Alterar dados Pessoais│")
        print("│5 - Voltar para a agenda  │")
        if(self.usuario.logado):
            print("│6 - Enviar Email          │")            
        print("└──────────────────────────┘")
        print("{}".format(self.mensagem))
        self.mensagem = ""
        opcao = input("*Opção: ")
        return opcao
    def erroEnviarEmail(self):
        print("Você só pode acessar essa opção logado em uma conta gmail, entre novamente para acessar esse recurso")
        os.system("pause")

    def procurarCodigo(self, opcao:int = 1):
        if opcao == 1:
            print("Digite o número do código do contato para fazer alteração")
        elif opcao == 0:
            print("Digite o número do código do contato para deletar")
        elif opcao == 2:
            print("Digite o número do código do contato para enviar um email a ele")
        print("{}".format(self.mensagem))
        codigo = input("Código: ")
        self.mensagem = ""
        return codigo

    def formularioEmail(self, contato:ContatoDTO):
        os.system("cls")
        print("╔════════════════════════════════════════════╗")
        print("║Entre com as informações:                   ║")
        print("╠════════════════════════════════════════════╣")
        print("║Digite o assunto do Email                   ║")
        assunto = input("║Assunto: ")
        print("╠════════════════════════════════════════════╣")
        print("║Digite o corpo do email")
        mensagem = input("║Mensagem: ")
        print("╚════════════════════════════════════════════╝")
        msgParaPrint = "║"
        posicao = 0
        os.system("cls")
        print("╔{}╗".format("═"*109))
        print("║{:^109}║".format("Formato do email:"))
        print("╠{}╣".format("═"*109)) 
        print("║     De: {:<100}║".format(self.usuario.email))
        print("╠{}╣".format("═"*109)) 
        print("║   Para: {:<100}║".format(contato.numero))
        print("╠{}╣".format("═"*109)) 
        print("║Assunto: {:<100}║".format(assunto))
        print("╠{}╣".format("═"*109)) 
        print("║Corpo do Email:{}║".format(" "*94))
        for pos, caracter in enumerate(mensagem):
            if posicao == 100:
                msgParaPrint = "║\n║" + msgParaPrint
            msgParaPrint = msgParaPrint + caracter
            if(pos == len(mensagem)):
                msgParaPrint = msgParaPrint + "║"
            posicao = posicao + 1
        print(msgParaPrint)
        print("╚{}╝".format("═"*109))
        print("\n\nEnviando...")
        return (assunto, mensagem)
            
            

    def colocarMensagem(self, codigo:int):
        print("•")
        if codigo == 1:
            self.mensagem += "\n\t■ Digite uma opção númerica"
        elif codigo == 2:
            self.mensagem += "\n\t■ Opção inválida"
        elif codigo == 3:
            self.mensagem += "\n\t■ Código apenas pode ser númerico"
        elif codigo == 4:
            self.mensagem += "\n\t■ Código de contato inválido"
        elif codigo == 5:
            self.mensagem += "\n\t■ Opção não tem Caractere(s) Especial(is)"
        elif codigo == 6:
            self.mensagem += "\n\t■ Código não tem Caractere(s) Especial(is)"
        elif codigo == 7:
            self.mensagem += "\n\t■ Por favor, preencha o  campo"
        else:
            self.mensagem += "\n\t■ Erro não identificado" 
