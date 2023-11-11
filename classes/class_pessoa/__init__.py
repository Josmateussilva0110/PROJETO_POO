class Pessoa():
    def __init__(self, cpf, nome, email, senha):
        self._cpf = cpf
        self._nome = nome
        self._email = email
        self._senha = senha
    
    @property
    def cpf(self):
        return self._cpf
    

    @property
    def nome(self):
        return self._nome
    

    @property
    def email(self):
        return self._email
    

    @property
    def senha(self):
        return self._senha


    @cpf.setter
    def cpf(self, valor):
        self._cpf = valor


    @nome.setter
    def cpf(self, valor):
        self._nome = valor 
    

    @email.setter
    def cpf(self, valor):
        self._email = valor
    

    @senha.setter
    def cpf(self, valor):
        self._senha = valor

