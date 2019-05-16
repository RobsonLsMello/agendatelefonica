import sqlite3

class DAO:
    def __init__(self):
        self.conexao = sqlite3.connect("banco.db")
        self.criarTabelas()
        self.inserirDadosBasicos()

    def criarTabelas(self):
        self.conexao.execute(
                    "CREATE TABLE IF NOT EXISTS tb_tipo_contato("+
                        "cd_tipo_contato INT PRIMARY KEY,"+
                        "nm_tipo_contato VARCHAR(100));")
        self.conexao.execute(
                    "CREATE TABLE IF NOT EXISTS tb_pessoa("+
                        "cd_pessoa INT PRIMARY KEY,"+
                        "nm_pessoa VARCHAR(100));")
        self.conexao.execute(           
                    "CREATE TABLE IF NOT EXISTS tb_contato("+
                        "cd_contato INT PRIMARY KEY,"+
                        "ds_contato varchar(100),"+
                        "cd_tipo_contato int,"+
                        "cd_pessoa int,"+
                        "FOREIGN KEY(cd_tipo_contato) references tb_tipo_contato(cd_tipo_contato),"+
                        "FOREIGN KEY(cd_pessoa) references tb_pessoa(cd_pessoa)"+
                    ");")

    def inserirTiposContatos(self):
        self.conexao.execute("insert into tb_tipo_contato values (0, 'Telefone')")
        self.conexao.execute("insert into tb_tipo_contato values (1, 'Celular')")
        self.conexao.execute("insert into tb_tipo_contato values (2, 'Email')")
        self.conexao.commit()

    def inserirPrimeirosItem(self):
        self.conexao.execute("insert into tb_pessoa values (0, 'Padrão')")
        self.conexao.commit()
        self.conexao.execute("insert into tb_contato values (0, '0000-0000', 0, 0)")
        self.conexao.commit()
        

    def inserirDadosBasicos(self):
        quantidade = self.conexao.execute("Select count(*) from tb_pessoa").fetchall()
        if(quantidade[0][0] == 0):
            self.inserirTiposContatos()
            self.inserirPrimeirosItem()