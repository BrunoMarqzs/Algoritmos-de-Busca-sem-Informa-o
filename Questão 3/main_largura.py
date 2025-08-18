from largura import No, Problema, BuscaLargura, estados_romenia
# Configuração do problema
no_arad = No('Arad', 0)
problema_romenia = Problema(
    inicial=no_arad,
    objetivo=lambda no: no.estado == 'Bucharest',
    espaco_estados=estados_romenia
)

# Execução da busca
bfs = BuscaLargura(problema_romenia)

print("BFS criada, iniciando busca...")
bfs.passo_busca()
bfs.passo_busca()
bfs.passo_busca()
bfs.passo_busca()
bfs.passo_busca()
bfs.passo_busca()
bfs.passo_busca()
bfs.passo_busca()
bfs.passo_busca()

print("Fronteira atual:", bfs.mostra_fronteira())
print("Solução parcial:",  bfs.mostra_solucao())
