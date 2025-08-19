romenia = {
    "Arad": ["Zerind", "Sibiu", "Timisoara"],
    "Zerind": ["Arad", "Oradea"],
    "Oradea": ["Zerind", "Sibiu"],
    "Sibiu": ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"],
    "Timisoara": ["Arad", "Lugoj"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Mehadia": ["Lugoj", "Drobeta"],
    "Drobeta": ["Mehadia", "Craiova"],
    "Craiova": ["Drobeta", "Rimnicu Vilcea", "Pitesti"],
    "Rimnicu Vilcea": ["Sibiu", "Craiova", "Pitesti"],
    "Fagaras": ["Sibiu", "Bucareste"],
    "Pitesti": ["Rimnicu Vilcea", "Craiova", "Bucareste"],
    "Bucareste": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"],
    "Giurgiu": ["Bucareste"],
    "Urziceni": ["Bucareste"]
}

def busca_em_largura(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]

    fronteira = [[inicio]]
    explorados = set()

    while fronteira:
        caminho = fronteira.pop(0)
        no_atual = caminho[-1]

        print("Visitando:", no_atual)
        explorados.add(no_atual)

        for vizinho in grafo[no_atual]:
            if vizinho not in explorados:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)

                if vizinho == objetivo:
                    return novo_caminho

                fronteira.append(novo_caminho)

    return None


inicio = "Oradea"
objetivo = "Craiova"

rota = busca_em_largura(romenia, inicio, objetivo)

print("\nRota encontrada (BFS):")
print(" -> ".join(rota))
