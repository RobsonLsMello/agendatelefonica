from Model.DAO.DAO import DAO
from Model.DTO.ContatoDTO import ContatoDTO
from Model.DTO.TipoContatoDTO import TipoContatoDTO
from Model.DTO.PessoaDTO import PessoaDTO

class AgendaDAO(DAO):
    def __init__(self):
        super().__init__()
        
    def criaPessoa(self, pessoa:PessoaDTO):
        self.conexao.execute("Insert into tb_pessoa select max(cd_pessoa) + 1, \"{}\" from tb_pessoa;".format(pessoa.nome))
        self.conexao.commit()

    def atualizarPessoa(self, pessoa:PessoaDTO):
        self.conexao.execute("update tb_pessoa set nm_pessoa = \"{}\" where cd_pessoa = \"{}\";".format(pessoa.nome, pessoa.codigo))
        self.conexao.commit()

    def selecionaPessoa(self, nome:str, ultimo:bool, codigo:int = -1):
        if ultimo == False and codigo == -1:
            pessoasSelecionadas = self.conexao.execute("Select * from tb_pessoa where nm_pessoa like \"%{}%\" order by nm_pessoa".format(nome)).fetchall()
        elif ultimo == False and codigo != -1:
            pessoasSelecionadas = self.conexao.execute("Select * from tb_pessoa where cd_pessoa = {}".format(codigo)).fetchall()
        else:
            pessoasSelecionadas = self.conexao.execute("Select * from tb_pessoa where cd_pessoa = (select max(cd_pessoa) from tb_pessoa)").fetchall()            
        pessoas = []
        for pessoaEncontrada in pessoasSelecionadas:
            pessoas.append(PessoaDTO(pessoaEncontrada[0], pessoaEncontrada[1], ""))
        return pessoas
    
    def deletaPessoa(self, pessoa:PessoaDTO):
        self.conexao.execute("delete from tb_contato where cd_pessoa = \"{}\"".format(pessoa.codigo))
        self.conexao.execute("delete from tb_pessoa where cd_pessoa = \"{}\"".format(pessoa.codigo))
        self.conexao.commit()

    def criaContato(self, contato:ContatoDTO):
        self.conexao.execute("Insert into tb_contato select max(cd_contato) +1, \"{}\", {}, {} from tb_contato".format(contato.numero, contato.tipoContato.codigo, contato.pessoa.codigo))
        self.conexao.commit()

    def alteraContato(self, contato:ContatoDTO):
        self.conexao.execute("update tb_contato set ds_contato = \"{}\", cd_tipo_contato = \"{}\" where cd_contato = \"{}\" ".format(contato.numero, contato.tipoContato.codigo, contato.codigo))
        self.conexao.commit()

    def deletaContato(self, contato:ContatoDTO):
        self.conexao.execute("delete from tb_contato where cd_contato = \"{}\"".format(contato.codigo))
        self.conexao.commit()

    def selecionaContato(self, pessoa:PessoaDTO, opcao:int = 0):
        if   opcao == 1:
            contatosSelecionados = self.conexao.execute("Select c.cd_contato, c.ds_contato, t.nm_tipo_contato from tb_contato as c join tb_tipo_contato as t on c.cd_tipo_contato = t.cd_tipo_contato where c.cd_pessoa = {} and c.cd_tipo_contato = 2".format(pessoa.codigo)).fetchall()
        elif opcao == 2:
            contatosSelecionados = self.conexao.execute("Select c.cd_contato, c.ds_contato, t.nm_tipo_contato from tb_contato as c join tb_tipo_contato as t on c.cd_tipo_contato = t.cd_tipo_contato where c.cd_contato = {}".format(pessoa.codigo)).fetchall()
        elif opcao == 0:
            contatosSelecionados = self.conexao.execute("Select c.cd_contato, c.ds_contato, t.nm_tipo_contato from tb_contato as c join tb_tipo_contato as t on c.cd_tipo_contato = t.cd_tipo_contato where c.cd_pessoa = {}".format(pessoa.codigo)).fetchall()
        contatos = []
        for contatoEncontrado in contatosSelecionados:
            contatos.append(ContatoDTO(contatoEncontrado[0], contatoEncontrado[1], 0, contatoEncontrado[2], pessoa.codigo))
        pessoa.contatos = contatos
        return pessoa

    def atualizaContato(self):
        pass

    def selecionaTiposContato(self):
        tiposEncontrados = self.conexao.execute("Select cd_tipo_contato, nm_tipo_contato from tb_tipo_contato").fetchall()
        tipos = []
        for tipo in tiposEncontrados:
            tipos.append(TipoContatoDTO(tipo[0], tipo[1]))
        return tipos