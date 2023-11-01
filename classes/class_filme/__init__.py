class Filme():
    def __init__(self, nome, ano, preco, classificacao, horarios, tipo):
        self._nome = nome
        self._ano = ano
        self._preco = preco
        self._classificacao = classificacao
        self._horarios = str(horarios)  # Agora, horários são uma string
        self._tipo = tipo
    

    def ver_filme(self):
        pass
    
