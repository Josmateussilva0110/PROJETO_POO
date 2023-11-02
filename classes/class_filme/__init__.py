class Filme():
    def __init__(self, nome, ano, preco, classificacao, horarios):
        self._nome = nome
        self._ano = ano
        self._preco = preco
        self._classificacao = classificacao
        self._horarios = str(horarios)  # Agora, horários são uma string

    def ver_filme(self):
        pass
    
