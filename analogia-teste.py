from abc import ABC, abstractmethod
from symtable import Class


class Universidades(ABC):

    def __init__(self):
        self.bolsista = []
        self.alunos = []

    @abstractmethod
    def add_bolsista(self, aluno):
        self.bolsista.append(aluno)
        return self.bolsista

    @abstractmethod
    def add_aluno(self, aluno):
        self.alunos.append(aluno)
        return self.alunos

class unieuro(Universidades):
    def __init__(self):
        super().__init__()

    def add_bolsista(self, aluno):




if __name__ == '__main__':


    aluno = aluno()
    aluno.unieuro()