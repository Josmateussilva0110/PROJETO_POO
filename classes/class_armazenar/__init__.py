class Armazenar():
    def __init__(self):
        self._dados = dict()
    
    def armazenar(self, pessoa):
        self._dados[pessoa._cpf] = pessoa
    

    def exibir_pessoa(self):
        for i, v in self._dados.items():
            print(f'{i} - {v._nome} - {v._email}')
