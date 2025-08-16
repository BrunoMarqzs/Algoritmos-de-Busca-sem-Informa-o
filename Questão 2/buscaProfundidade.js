import { No } from './estadoRomenia.js';

// constantes para situação da busca
const BUSCA_INICIANDO = 0;
const BUSCA_EM_CURSO = 1;
const BUSCA_FALHA = 2;
const BUSCA_SUCESSO = 3;

export class BuscaProfundidade {
    constructor(problema) {
        this.problema = problema;
        this.fronteira = [problema.inicial]; // pilha
        this.visitados = [problema.inicial.estado];
        this.situacao = BUSCA_INICIANDO;
        this.solucao = [];
    }

    // Método para executar a DFS passo a passo
    passoBusca() {
        if (this.situacao === BUSCA_FALHA) {
            console.log("Busca falhou");
            return;
        }
        if (this.situacao === BUSCA_SUCESSO) {
            console.log("Solução já encontrada");
            return;
        }

        let no = this.fronteira.pop(); // DFS: pega o último nó da pilha
        if (!no) {
            this.situacao = BUSCA_FALHA;
            console.log("Fronteira vazia. Busca falhou");
            return;
        }

        console.log(`No atual: (${no.estado}, ${no.custo})`);

        if (this.problema.objetivo(no)) {
            this.solucao = no.constroiSolucao();
            this.situacao = BUSCA_SUCESSO;
            console.log("Solução encontrada!");
            return;
        }

        for (let filho of no.filhos(this.problema)) {
            if (!this.fronteira.some(n => n.estado === filho.estado) &&
                !this.visitados.includes(filho.estado)) {
                this.fronteira.push(filho);   // DFS adiciona ao topo da pilha
                this.visitados.push(filho.estado);
            }
        }

        this.situacao = BUSCA_EM_CURSO;
    }

    visitado(estado) {
        return this.visitados.includes(estado);
    }

    mostraSolucao() {
        if (this.solucao.length === 0) return "Nenhuma solução ainda.";
        return this.solucao.map(n => `(${n.estado}, ${n.custo})`).join(' -> ') +
               ` | Custo: ${this.solucao[this.solucao.length - 1].custo}`;
    }

    mostraFronteira() {
        return '[' + this.fronteira.map(n => `(${n.estado}, ${n.custo})`).join(" ") + ']';
    }
}


