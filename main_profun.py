from profundidade import No, Problema, BuscaProfundidade, estados_romenia

# Configuração do problema
no_arad = No('Arad', 0)
problema_romenia = Problema(
    inicial=no_arad,
    objetivo=lambda no: no.estado == 'Bucharest',
    espaco_estados=estados_romenia
)

# Execução da busca
dfs = BuscaProfundidade(problema_romenia)

print("DFS criada, iniciando busca...")
dfs.passo_busca()  
dfs.passo_busca()
dfs.passo_busca()
dfs.passo_busca()
dfs.passo_busca()
dfs.passo_busca()
dfs.passo_busca()
dfs.passo_busca()

print("Fronteira atual:", dfs.mostra_fronteira())
print("Solução parcial:", dfs.mostra_solucao())