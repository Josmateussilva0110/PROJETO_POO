class Filme():
    def __init__(self, id, nome, ano, preco, classificacao, horario, tipo):
        self._id = id
        self._nome = nome
        self._ano = ano
        self._preco = preco
        self._classificacao = classificacao
        self._horario = horario
        self._tipo = tipo
    

    def ver_filme(self):
        print(f'id:{self._id}\nnome: {self._nome}\nano: {self._ano}\npreco: {self._preco}\nclassificao: {self._classificacao}\nhorario: {self._horario}')
