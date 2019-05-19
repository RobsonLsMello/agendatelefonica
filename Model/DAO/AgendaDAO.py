from Model.DAO.DAO import DAO
from Model.DTO.ContatoDTO import ContatoDTO
from Model.DTO.PessoaDTO import PessoaDTO

class AgendaDAO(DAO):
    def __init__(self):
        super().__init__()
        
    def criaPessoa(self, pessoa:PessoaDTO):
        self.conexao.execute("Insert into tb_pessoa select max(cd_pessoa) + 1, \"{}\" from tb_pessoa;".format(pessoa.nome))
        self.conexao.commit()

    def selecionaPessoa(self, nome:str, ultimo:bool, codigo:int = -1):
        if ultimo == False and codigo == -1:
            pessoasSelecionadas = self.conexao.execute("Select * from tb_pessoa where nm_pessoa like \"%{}%\"".format(nome)).fetchall()
        elif ultimo == False and codigo != -1:
            pessoasSelecionadas = self.conexao.execute("Select * from tb_pessoa where cd_pessoa = {}".format(codigo)).fetchall()
        else:
            pessoasSelecionadas = self.conexao.execute("Select * from tb_pessoa where cd_pessoa = (select max(cd_pessoa) from tb_pessoa)").fetchall()            
        pessoas = []
        for pessoaEncontrada in pessoasSelecionadas:
            pessoas.append(PessoaDTO(pessoaEncontrada[0], pessoaEncontrada[1], ""))
        return pessoas
        

    def criaContato(self, contato:ContatoDTO):
        self.conexao.execute("Insert into tb_contato values (?,?,?,?)", (contato.codigo, contato.numero, contato.tipoContato.codigo, contato.pessoa.codigo))
        self.conexao.commit()
        pass

    def deletaContato(self):
        pass

    def selecionaContato(self, pessoa:PessoaDTO):
        contatosSelecionados = self.conexao.execute("Select c.cd_contato, c.ds_contato, t.nm_tipo_contato from tb_contato as c join tb_tipo_contato as t on c.cd_tipo_contato = t.cd_tipo_contato where c.cd_pessoa = {}".format(pessoa.codigo)).fetchall()
        contatos = []
        for contatoEncontrado in contatosSelecionados:
            contatos.append(ContatoDTO(contatoEncontrado[0], contatoEncontrado[1], 0, contatoEncontrado[2], pessoa.codigo))
        pessoa.contatos = contatos
        return pessoa

    def atualizaContato(self):
        pass