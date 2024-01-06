class Filme():
    """
    Classe que representa um filme com informações básicas.

    Attributes
    ------------
        nome : str
            Nome do filme.
        ano : str
            Ano de lançamento do filme.
        preco : float
            Preço do ingresso para o filme.
        classificacao : str
            Classificação indicativa do filme.
        horarios : str 
            Horários de exibição do filme, representados como uma string.
    """
    def __init__(self, nome, ano, preco, classificacao, horarios):
        self._nome = nome
        self._ano = ano
        self._preco = preco
        self._classificacao = classificacao
        self._horarios = str(horarios)   # Agora, horários são uma string
    def ver_filme(self):
        pass
    
