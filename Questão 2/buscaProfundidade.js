export class BuscaProfundidade {
    constructor(problema) {
        this.problema = problema;
        this.fronteira = [problema.inicial]; // DFS usa stack, pop do final
        this.visitados = [problema.inicial.estado];
        this.solucao = [];
    }

    efetuarBusca() {
        console.log("Iniciando DFS...");

        while (this.fronteira.length > 0) {
            this.passoBusca();
        }

        if (this.solucao.length === 0) {
            console.log("Busca falhou: não encontrou solução.");
        } else {
            console.log("Solução encontrada:");
            console.log(this.mostraSolucao());
        }
    }

    passoBusca() {
        const no = this.fronteira.pop(); // DFS: remove do topo
        console.log("No atual:", no.toString());

        if (this.problema.objetivo(no)) {
            this.solucao = no.constroiSolucao();
            // Limpa fronteira para sair do while
            this.fronteira = [];
            return;
        }

        for (const filho of no.filhos(this.problema)) {
            if (!this.visitados.includes(filho.estado)) {
                this.fronteira.push(filho);
                this.visitados.push(filho.estado);
            }
        }
    }

    mostraSolucao() {
        return this.solucao.map(n => n.toString()).join(" -> ") +
               ` | Custo: ${this.solucao[this.solucao.length - 1].custo}`;
    }
}
