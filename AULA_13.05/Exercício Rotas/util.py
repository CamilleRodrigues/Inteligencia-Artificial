import random

class Util:
    cidades = [1,2,3,4,5,6,7,8,9]

    @staticmethod
    def gerar_rota():
        #não repete cidades, embaralha automaticamente, já cria uma permutação válida
        return random.sample (Util.cidades, len(Util.cidades))
        
