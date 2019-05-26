# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Model.DTO.UsuarioDTO import UsuarioDTO
import smtplib
#python.agenda@gmail.com
#SucoDeUva#1

class EnviarEmail:
    def __init__(self):
        self.msg = MIMEMultipart()
        self.mensagem = ""
 
    def setMensagem(self, mensagem:str):
        self.mensagem = mensagem
 
    def setDadosRemetente(self, usuario:UsuarioDTO):
        self.password = usuario.senha
        self.msg['From'] = usuario.email

    def setDadosDestinario(self, email:str, assunto:str):
        self.msg['To'] = email
        self.msg['Subject'] = assunto
    
    def enviarEmail(self):
        erro = 0
        try:
            # add in the message body
            self.msg.attach(MIMEText(self.mensagem, 'plain'))
            #create server
            server = smtplib.SMTP_SSL('smtp.gmail.com')
            #server.starttls()
            # Login Credentials for sending the mail
            server.login(self.msg['From'], self.password)
            # send the message via the server.
            server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
            server.quit()
        except smtplib.SMTPAuthenticationError:
            erro = 1
        except smtplib.SMTPServerDisconnected:
            erro = 2
        except Exception:
            erro = 3
        return erro