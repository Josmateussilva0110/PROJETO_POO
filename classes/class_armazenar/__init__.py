class Armazenar():
    def __init__(self):
        self._dados = dict()
    
    def armazenar(self, pessoa):
        self._dados[pessoa._cpf] = pessoa
    

    def exibir_pessoa(self):
        for i, v in self._dados.items():
            print(f'{i} - {v._nome} - {v._cpf} - {v._email} - {v._senha}')

    def verificar_login(self, cpf, senha):
        for pessoa in self._dados.values():
            if pessoa._cpf == cpf and pessoa._senha == senha:
                return True
        return False

