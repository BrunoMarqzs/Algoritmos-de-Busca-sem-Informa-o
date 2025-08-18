class No:
    def __init__(self, estado, custo, pai=None, acao=None):
        self.estado = estado
        self.custo = custo
        self.pai = pai
        self.acao = acao

    def __repr__(self):
        return f"({self.estado}, {self.custo})"

    def filhos(self, problema):
        estado_acoes = next((ea for ea in problema.espaco_estados if ea['estado'] == self.estado), None)
        if not estado_acoes:
            return []
        return [No(a['destino'], self.custo + a['custo'], self, a['destino']) for a in estado_acoes['acoes']]

    def constroi_solucao(self):
        no = self
        solucao = []
        while no:
            solucao.insert(0, no)
            no = no.pai
        return solucao


class Problema:
    def __init__(self, inicial, objetivo, espaco_estados):
        self.inicial = inicial
        self.objetivo = objetivo
        self.espaco_estados = espaco_estados

    def objetivo_alcancado(self, no):
        return self.objetivo(no)


class BuscaProfundidade:
    BUSCA_INICIANDO = 0
    BUSCA_EM_CURSO = 1
    BUSCA_FALHA = 2
    BUSCA_SUCESSO = 3

    def __init__(self, problema):
        self.problema = problema
        self.fronteira = [problema.inicial]  # pilha
        self.visitados = [problema.inicial.estado]
        self.situacao = self.BUSCA_INICIANDO
        self.solucao = []

    def passo_busca(self):
        if self.situacao == self.BUSCA_FALHA:
            print("Busca falhou")
            return
        if self.situacao == self.BUSCA_SUCESSO:
            print("Solução já encontrada")
            return

        if not self.fronteira:
            self.situacao = self.BUSCA_FALHA
            print("Fronteira vazia. Busca falhou")
            return

        no = self.fronteira.pop()  # DFS: pega o último nó da pilha
        print(f"Nó atual: ({no.estado}, {no.custo})")

        if self.problema.objetivo_alcancado(no):
            self.solucao = no.constroi_solucao()
            self.situacao = self.BUSCA_SUCESSO
            print("Solução encontrada!")
            return

        for filho in no.filhos(self.problema):
            if filho.estado not in self.visitados and not any(n.estado == filho.estado for n in self.fronteira):
                self.fronteira.append(filho)  # DFS adiciona ao topo da pilha
                self.visitados.append(filho.estado)

        self.situacao = self.BUSCA_EM_CURSO

    def mostra_solucao(self):
        if not self.solucao:
            return "Nenhuma solução ainda."
        return " -> ".join([f"({n.estado}, {n.custo})" for n in self.solucao]) + \
               f" | Custo: {self.solucao[-1].custo}"

    def mostra_fronteira(self):
        return "[" + " ".join([f"({n.estado}, {n.custo})" for n in self.fronteira]) + "]"


# Estados e suas ações
estados_romenia = [
    {'estado': 'Arad', 'acoes': [{'destino': 'Zerind', 'custo': 75}, {'destino': 'Sibiu', 'custo': 140}, {'destino': 'Timisoara', 'custo': 118}]},
    {'estado': 'Zerind', 'acoes': [{'destino': 'Arad', 'custo': 75}, {'destino': 'Oradea', 'custo': 71}]},
    {'estado': 'Timisoara', 'acoes': [{'destino': 'Arad', 'custo': 118}, {'destino': 'Lugoj', 'custo': 111}]},
    {'estado': 'Sibiu', 'acoes': [{'destino': 'Arad', 'custo': 140}, {'destino': 'Oradea', 'custo': 151}, {'destino': 'Fagaras', 'custo': 99}, {'destino': 'Rimnicu Vilcea', 'custo': 80}]},
    {'estado': 'Oradea', 'acoes': [{'destino': 'Zerind', 'custo': 71}, {'destino': 'Sibiu', 'custo': 151}]},
    {'estado': 'Lugoj', 'acoes': [{'destino': 'Timisoara', 'custo': 111}, {'destino': 'Mehadia', 'custo': 70}]},
    {'estado': 'Mehadia', 'acoes': [{'destino': 'Lugoj', 'custo': 70}, {'destino': 'Drobeta', 'custo': 75}]},
    {'estado': 'Drobeta', 'acoes': [{'destino': 'Mehadia', 'custo': 75}, {'destino': 'Craiova', 'custo': 120}]},
    {'estado': 'Craiova', 'acoes': [{'destino': 'Drobeta', 'custo': 120}, {'destino': 'Rimnicu Vilcea', 'custo': 146}, {'destino': 'Pitesti', 'custo': 138}]},
    {'estado': 'Rimnicu Vilcea', 'acoes': [{'destino': 'Sibiu', 'custo': 80}, {'destino': 'Craiova', 'custo': 146}, {'destino': 'Pitesti', 'custo': 97}]},
    {'estado': 'Fagaras', 'acoes': [{'destino': 'Sibiu', 'custo': 99}, {'destino': 'Bucharest', 'custo': 211}]},
    {'estado': 'Pitesti', 'acoes': [{'destino': 'Rimnicu Vilcea', 'custo': 97}, {'destino': 'Craiova', 'custo': 138}, {'destino': 'Bucharest', 'custo': 101}]},
    {'estado': 'Giurgiu', 'acoes': [{'destino': 'Bucharest', 'custo': 90}]},
    {'estado': 'Bucharest', 'acoes': [{'destino': 'Fagaras', 'custo': 211}, {'destino': 'Pitesti', 'custo': 101}, {'destino': 'Giurgiu', 'custo': 90}, {'destino': 'Urziceni', 'custo': 85}]},
    {'estado': 'Urziceni', 'acoes': [{'destino': 'Bucharest', 'custo': 85}, {'destino': 'Vaslui', 'custo': 142}, {'destino': 'Hirsova', 'custo': 98}]},
    {'estado': 'Hirsova', 'acoes': [{'destino': 'Urziceni', 'custo': 98}, {'destino': 'Eforie', 'custo': 86}]},
    {'estado': 'Eforie', 'acoes': [{'destino': 'Hirsova', 'custo': 86}]},
    {'estado': 'Vaslui', 'acoes': [{'destino': 'Urziceni', 'custo': 142}, {'destino': 'Iasi', 'custo': 92}]},
    {'estado': 'Iasi', 'acoes': [{'destino': 'Vaslui', 'custo': 92}, {'destino': 'Neamt', 'custo': 87}]},
    {'estado': 'Neamt', 'acoes': [{'destino': 'Iasi', 'custo': 87}]}
]


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
