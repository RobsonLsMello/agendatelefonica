from Model.DTO.PessoaDTO import PessoaDTO
class PrincipalView:
    def __init__(self):
        print("\t\tAgenda dos MONSTROS\n\n")

    def menu(self, agenda):
        opcao = -1
        print("|Codigo\t|Nome\t\t|\n")
        for pessoa in agenda:
            print("|{}\t|{}\t\t|".format(pessoa.codigo, pessoa.nome))
        print("Você deseja?\n1-Adicionar Contatos\n2-Selecionar Contato\n3-Procurar Contato")
        while(opcao < 0 or opcao > 2):
            opcao = int(input("Opção: "))
            if opcao < 0 or opcao > 2:
                print("Opção inválida, por favor, digite novamente")
        return opcao

