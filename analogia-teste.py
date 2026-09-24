from abc import ABC, abstractmethod
from symtable import Class


class Universidades(ABC):

    def __init__(self):
        self.bolsista = []
        self.alunos = []

    @abstractmethod
    def add_bolsista(self):
        pass

    @abstractmethod
    def add_aluno(self):
        pass





class unieuro(Universidades):
    def __init__(self):
        super().__init__()

    def add_bolsista(self, bolsista):
        self.bolsista.append(bolsista)
        return self.bolsista

    def add_aluno(self, aluno):
        self.alunos.append(aluno)
        return self.alunos

    
# TENHO QUE ADD UMA VALIDACAO PARA CALCULAR VALOR DE PARCELA SE BOLSISTA SE NAO PAGA VALOR NORMAL
# VALIDAR SE BOLSISTA É ALUNO.
# BOLSISTA PRECISA EST ANA LISTA DE ALUNOS PARA SER ADICIONADO NA LISTA DE BOLSISTAS

if __name__ == '__main__':


    aluno = unieuro()
    aluno.add_bolsista("hallisson")
    aluno.add_aluno("hallisson")