from Model.DAO.DAO import DAO
from Model.DTO.ContatoDTO import ContatoDTO
from Model.DTO.PessoaDTO import PessoaDTO

class AgendaDAO(DAO):
    def __init__(self):
        super().__init__()
        
    def criaPessoa(self, pessoa:PessoaDTO):
        self.conexao.execute("Insert into tb_pessoa select max(cd_pessoa) + 1, \"{}\" from tb_pessoa;".format(pessoa.nome))
        #self.conexao.commit()

    def selecionaPessoa(self, nome):
        pessoasSelecionadas = self.conexao.execute("Select * from tb_pessoa where nm_pessoa like \"%{}%\"".format(nome)).fetchall()
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

    def selecionaContato(self, nome):
        contatosSelecionados = self.conexao.execute("Select * from tb_contato where ds_contato = ?", (nome)).fetchall()
        for contatoEncontrado in contatosSelecionados:
            print(contatoEncontrado)

    def atualizaContato(self):
        pass