class UsuarioDTO:
    def __init__(self, email:str, senha:str, logado:bool = False):
        self.email = email
        self.senha = senha
        self.logado = logado