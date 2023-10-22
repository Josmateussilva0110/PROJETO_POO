class Armazenar():
    def __init__(self):
        self._dados = dict()
        self._dados_func = dict()
    
    def armazenar(self, pessoa):
        self._dados[pessoa._cpf] = pessoa
        
    def armazena_func(self,func):
        self._dados_func[func._cpf] = func
    

    def exibir_pessoa(self):
        print('pessoa')
        for i, v in self._dados.items():
            print(f'{i} - {v._nome} - {v._cpf} - {v._email} - {v._senha}')
            
    def exibir_fnc(self):
        print('Fuucionario')    
        for i, v in self._dados_func.items():
            print(f'{i} - {v._nome} - {v._cpf} - {v._email} - {v._senha}')

    def verificar_login(self, cpf, senha):
        for pessoa in self._dados.values():
            if pessoa._cpf == cpf and pessoa._senha == senha:
                return True
        return False
    
    def verificar_login_func(self, cpf, senha):
        for pessoa in self._dados_func.values():
            if pessoa._cpf == cpf and pessoa._senha == senha:
                return True
        return False
