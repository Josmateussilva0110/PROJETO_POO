class Armazenar():
    def __init__(self):
        self._dados = dict()
        self._dados_func = dict()
        self._dados_filmes = dict()
    
    def armazenar(self, pessoa, cpf):
        if cpf not in self._dados and cpf not in self._dados_func:
            self._dados[cpf] = pessoa
            return True
        else:
            return False
        
    def armazena_func(self,func, cpf):
        if cpf not in self._dados and cpf not in self._dados_func:
            self._dados_func[cpf] = func
            return True
        else:
            return False
    
    def armazenar_filme(self, filme, id):
        if id not in self._dados_filmes:
            self._dados_filmes[id] = filme
            return True
        else:
            return False
    

    def exibir_pessoa(self):
        print('pessoa')
        for i, v in self._dados.items():
            print(f'{i} - {v._nome} - {v._cpf} - {v._email} - {v._senha}')
            
    def exibir_fnc(self):
        print('Funcionario')    
        for i, v in self._dados_func.items():
            print(f'{i} - {v._nome} - {v._cpf} - {v._email} - {v._senha}')

    def verificar_login_Cliente(self, cpf, senha):
        for pessoa in self._dados.values():
            if pessoa._cpf == cpf and pessoa._senha == senha:
                return True
        return False
    
    def verificar_login_Ger(self, cpf, senha):
        for pessoa in self._dados_func.values():
            if pessoa._cpf == cpf and pessoa._senha == senha:
                return True
        return False
    
    def buscar_filme(self, id):
        for i in self._dados_filmes.keys():
            if i == id:
                return self._dados_filmes[id]
        return None
