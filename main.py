from datetime import date

#hoje = date.today()

class aluno:

    def __init__(self, ):
        self.nome: str = ""
        self.matricula: int = 0
        self.nascimento: str = ""
        self.data = date.today()


    def aniversario(self):

            if self.nascimento == hoje:
                print(f"Parabéns {self.nome}. É seu aniversario")
                print("!!!!!!!FELIZ ANIVERSARIO!!!!!")

    def cadastrar(self):
        print("Olá bem vindo a Anhanguera!")


        print("=== CADASTRAR ALUNO ===")
        self.nome = input("Qual o seu nome: ")
        # MATRICULO VOU DEIXAR PARA GERAR AUTOMATICO.
        self.nascimento = input("Qual a sua data de nascimento: ")
        self.


if __name__ == '__main__':

    aluno = aluno()

