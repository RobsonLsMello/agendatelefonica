from Lib.TextoUtil import TextoUtil

class Validador:
    def __init__(self):
        self.mensagem = ""
        self.erro = 0

    def validarEmail(self, email:str):
        erroDeFormato = False
        if(len(email) > 100):
            self.colocarMensagemErro(8)
            erroDeFormato = True
        if(len(email) < 5):
            self.colocarMensagemErro(14)
            erroDeFormato = True
        if(email.find('.') == -1):
            self.colocarMensagemErro(9)
            erroDeFormato = True
        aposarroba = ""
        antesarroba = ""
        if(email.find('@') == -1):
            self.colocarMensagemErro(10)
            erroDeFormato = True
        else:
            conteudoEntreArroba = email.split("@")
            aposarroba = conteudoEntreArroba[1]
            antesarroba = conteudoEntreArroba[0]
            if(aposarroba.find('.') == -1):
                self.colocarMensagemErro(15)
                erroDeFormato = True
            if(antesarroba == ""):
                self.colocarMensagemErro(18)
                erroDeFormato = True
        if(antesarroba != ""):
            if(TextoUtil().verificarTextoComCaracteresEspeciais(antesarroba[0]) or antesarroba[0] == " "):
                self.colocarMensagemErro(19)
                erroDeFormato = True
            if(TextoUtil().verificarTextoComCaracteresEspeciais(antesarroba[len(antesarroba) - 1])):
                self.colocarMensagemErro(20)
                erroDeFormato = True
        if(aposarroba  != ""):
            if(aposarroba.find('.') != -1):
                splitponto = aposarroba.split(".")
                if(splitponto[0] == ""):
                    self.colocarMensagemErro(16)
                    erroDeFormato = True
                if(splitponto[1] == ""):
                    self.colocarMensagemErro(17)
                    erroDeFormato = True
        if(email.find(" ") != -1):
            self.colocarMensagemErro(21)
            erroDeFormato = True
        return erroDeFormato, self.mensagem

    def colocarMensagemErro(self, codigo):
        if self.erro != 0:
            self.mensagem += "\n"
        else:
            self.mensagem += "║\t                                                   ║\n"
        if codigo == 8:
            self.mensagem += "║\t■ Contato pode ter até 100(cem) caracteres         ║"
        elif codigo == 9:
            self.mensagem += "║\t■ Um email precisa conter ao menos 1(um) \".\"       ║"
        elif codigo == 10:
            self.mensagem += "║\t■ Um email precisa conter ao menos 1(um) \"@\"       ║"
        elif codigo == 11:
            self.mensagem += "║\t■ Tipo de Contato não tem Caractere(s) Especial(is)║"
        elif codigo == 12:
            self.mensagem += "║\t■ Telefone não tem Caractere(s) Especial(is)       ║"
        elif codigo == 13:
            self.mensagem += "║\t■ Celular não tem Caractere(s) Especial(is)        ║"
        elif codigo == 14: #a@a.a
            self.mensagem += "║\t■ Email deve ter ao menos 5(cinco) caracteres      ║"
        elif codigo == 15:
            self.mensagem += "║\t■ Um email precisa conter ao menos um \".\" após do @║"
        elif codigo == 16:
            self.mensagem += "║\t■ Um email precisa conter um caracter antes do \".\" ║\n║\t\tque está após o @\t\t\t   ║"
        elif codigo == 17:
            self.mensagem += "║\t■ Um email precisa conter um caracter após do \".\"  ║\n║\t\tque está após o @\t\t\t   ║"
        elif codigo == 18:
            self.mensagem += "║\t■ Um email precisa conter ao menos 1(um) caracter  ║\n║\t\tantes do @       \t\t\t   ║"
        elif codigo == 19:
            self.mensagem += "║\t■ O primeiro caracter antes do @ deve ser apenas   ║\n║\t\tCaracter de aA - zZ ou 0-9\t\t   ║"
        elif codigo == 20:
            self.mensagem += "║\t■ O último caracter antes do @ deve ser apenas     ║\n║\t\tCaracter de aA - zZ ou 0-9\t\t   ║"
        elif codigo == 21:
            self.mensagem += "║\t■ Email pode ter \"espaço\" em branco                ║"  
        self.erro = self.erro + 1