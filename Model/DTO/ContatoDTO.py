#TipoContato
from Model.DTO.PessoaDTO import PessoaDTO
from Model.DTO.TipoContatoDTO import TipoContatoDTO  

class ContatoDTO:
    def __init__(self, codigo, numero,  codigoTipo, nomeTipo, codigoPessoa):
        self.codigo = codigo
        self.numero = numero        
        self.tipoContato = TipoContatoDTO(codigoTipo, nomeTipo)
        self.pessoa = PessoaDTO(codigoPessoa, "", "")