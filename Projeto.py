
from Controller.PrincipalController import PrincipalController
from Controller.LoginController import LoginController
import os

class Sistema:
    def __init__(self):
        self.definirTela()
        login = LoginController()
        login.index()
    
    def definirTela(self):
        os.system("title Agenda de Python")
        os.system("color 02")
        os.system("mode 150")
    
sistema = Sistema()
        
        
