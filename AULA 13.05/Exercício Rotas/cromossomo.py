class Cromossomo:

    def __init__(self, valor):
        self.valor = valor
        self.aptidao = self.calcular_aptidao()
    
    def calcular_aptidao(self):
        penalidade = 0
        for i in range(len(self.valor)):
           for j in range(i + 1, len(self.valor)):
               if self.valor[i] > self.valor[j]:
                   penalidade = penalidade + 10
    
        contagem = {}

        for cidade in self.valor:
            contagem[cidade] = contagem.get(cidade, 0) + 1

        for qtd in contagem.values():
            if qtd > 1:
                pares = qtd * (qtd - 1) // 2
                penalidade = penalidade + pares * 20

        return penalidade
    
    def __eq__(self, other):
        if isinstance(other, Cromossomo):
            return self.valor == other.valor
        return False
    
    def __lt__(self, other):
        return self.aptidao < other.aptidao
    
    def __str__(self):
        return f"rota = {self.valor}, aptidao = {self.aptidao}"
    

