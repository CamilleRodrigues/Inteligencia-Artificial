import random

from cromossomo import Cromossomo
from util import Util # type: ignore


class AG:
    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao):
        for i in range(tamanho_populacao):
            populacao.append(Cromossomo(Util.gerar_rota()))

    @staticmethod
    def exibir(populacao):
        for i in populacao:
            print(i)

    @staticmethod
    def selecionar_por_torneio(populacao, nova_populacao, taxa_selecao):
        torneio = []

        qtd_selecionados = int(taxa_selecao * len(populacao) / 100)

        melhor = populacao[0]

        nova_populacao.append(melhor)

        i = 1
        while i <= qtd_selecionados:
            c1 = populacao[random.randrange(len(populacao))]

            while True:
                c2 = populacao[random.randrange(len(populacao))]
                if c2 != c1:
                    break

            while True:
                c3 = populacao[random.randrange(len(populacao))]
                if c3 != c1 and c3 != c2:
                    break

            torneio.append(c1)
            torneio.append(c2)
            torneio.append(c3)

            torneio.sort()

            selecionado = torneio[0]

            if selecionado not in nova_populacao:
                nova_populacao.append(selecionado)
                i += 1

            torneio.clear()

    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao):
        qtd_reproduzidos = int(taxa_reproducao * len(populacao) / 100)

        i = 0
        while i < qtd_reproduzidos:
            pai = populacao[random.randrange(len(populacao))]

            while True:
                mae = populacao[random.randrange(len(populacao))]
                if mae != pai:
                    break

            p1 = pai.valor
            p2 = mae.valor

            ponto = random.randrange(1, len(p1) - 1)

            filho1 = p1[:ponto]
            for gene in p2:
                if gene not in filho1:
                    filho1.append(gene)

            filho2 = p2[:ponto]
            for gene in p1:
                if gene not in filho2:
                    filho2.append(gene)

            nova_populacao.append(Cromossomo(filho1))

            nova_populacao.append(Cromossomo(filho2))

            i += 2

        while len(nova_populacao) > len(populacao):
            nova_populacao.pop()

    @staticmethod
    def mutar(populacao):
        qtd_mutantes = random.randint(1, max(1, int(len(populacao) / 5)))

        while qtd_mutantes > 0:
            posicao_mutante = random.randrange(len(populacao))

            mutante = populacao[posicao_mutante]

            rota = mutante.valor.copy()

            a = random.randrange(len(rota))
            b = random.randrange(len(rota))

            rota[a], rota[b] = rota[b], rota[a]

            populacao[posicao_mutante] = (Cromossomo(rota))

            qtd_mutantes -= 1
