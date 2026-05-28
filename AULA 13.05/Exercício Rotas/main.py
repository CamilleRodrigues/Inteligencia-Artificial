import copy
import os

from ag import AG

os.system('cls')


tamanho_populacao = int(input("Tamanho da população: "))
taxa_selecao = int(input("Taxa de seleção (20 a 40%): "))
taxa_reproducao = 100 - taxa_selecao
taxa_mutacao = int(input("Taxa de mutação (5 a 10%): "))
qtd_geracoes = int(input("Quantidade de gerações: "))

populacao = []
nova_populacao = []

AG.gerar_populacao(populacao, tamanho_populacao)

populacao.sort()

print("\nGERAÇÃO 1")

AG.exibir(populacao)

for i in range(1, qtd_geracoes):
    AG.selecionar_por_torneio(populacao, nova_populacao, taxa_selecao)
    AG.reproduzir(populacao, nova_populacao, taxa_reproducao)

    if i % int(len(populacao) / taxa_mutacao) == 0:
        AG.mutar(nova_populacao)

    populacao = copy.deepcopy(nova_populacao)

    nova_populacao.clear()

    populacao.sort()

    print(f"\nGERAÇÃO {(i + 1)}")

    AG.exibir(populacao)

    melhor = populacao[0]

    if melhor.aptidao == 0:
        print(f"\nSolução encontrada na geração {(i + 1)}")
        print(melhor)
    else:
        print("\nNenhuma solução com aptidão igual a 0 foi encontrada.")
        print("Melhor solução encontrada:", populacao[0])


        break
