from Controller.PrincipalController import PrincipalController
import os

class Sistema:
    def __init__(self):
        self.definirTela()
        principal = PrincipalController()
    
    def definirTela(self):
        os.system("title Agenda de Python")
        os.system("color 02")
        os.system("mode 150")
    
sistema = Sistema()
        
        
