import sqlite3
class DAO:
    def __init__(self):
        self.conexao = sqlite3.connect("banco.db")
        self.criarTabelas()

    def criarTabelas(self):
        self.conexao.execute(
                    "CREATE TABLE IF NOT EXISTS tb_tipo_contato("+
                        "cd_tipo_contato INT PRIMARY KEY,"+
                        "nm_tipo_contato VARCHAR(100));")
        self.conexao.execute(
                "CREATE TABLE IF NOT EXISTS tb_usuario("+
                        "cd_usuario INT PRIMARY KEY,"+
                        "nm_usuario VARCHAR(100));")
        self.conexao.execute(           
                    "CREATE TABLE IF NOT EXISTS tb_conta("+
                        "cd_contato INT PRIMARY KEY,"+
                        "ds_contato varchar(100),"+
                        "cd_tipo_contato int,"+
                        "cd_usuario int,"+
                        "FOREIGN KEY(cd_tipo_contato) references tb_tipo_contato(cd_tipo_contato),"+
                        "FOREIGN KEY(cd_usuario) references tb_usuario(cd_usuario)"+
                    ");")

    def inserirTiposContatos(self):
        self.conexao.execute("insert into tb_tipo_contato values (0, 'Telefone')"):
        self.conexao.execute("insert into tb_tipo_contato values (1, 'Celular')"):
        self.conexao.execute("insert into tb_tipo_contato values (2, 'Email')"):
        

        
class TipoContato:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        
class Contato:
    def __init__(self, codigo, numero, nome,  codigoTipo):
        self.codigo = codigo
        self.nome = nome
        self.numero = numero        
        self.tipoContato = TipoContato()

class Usuario:
    def __init__(self, codigo, nome, contatos:List, agenda:Agenda)
        self.codigo = codigo
        self.nome = nome
        self.contatos = contatos
        self.agenda = agenda

    def criarUsuario:
        pass

    def alterarUsuario:
        pass

    def deletarUsuario:
        pass

        
        
        
class Agenda(DAO):
    def __init__(self):
        super().__init__()
        self.contatos = []
    
    def criaContatos(self, contato:Contato):
        self.conexao.execute("Insert into tb_contato values (?,?,?,?)", (contato.codigo,contato.nome, contato.numero, contato.tipoContato.codigo))
        self.conexao.commit()
        pass

    def deletaContatos():
        pass

    def selecionaContatos(self, nome):
        contatosSelecionados = self.conexao.execute("Select id, numero from tb_contato where nome = ?", (nome)).fetchall()
        for contatoEncontrado in contatosSelecionados:
            print(contatoEncontrado)

    def atualizaContatos():
        pass





class Sistema:
    def __init__(self):
        print("\t\tAgenda dos Filhos\n\n")
        self.menu()
        
        
    def menu(self):
        opcao = -1
        print("Você deseja?\n1-Visualizar Contatos\n2-Adicionar Contatos\n")
        while(opcao < 0 or opcao > 2):
            opcao = int(input("Opção: "))
            if opcao < 0 or opcao > 2:
                print("Opção inválida, por favor, digite novamente")
        return opcao

    
sistema = Sistema()
        
        
