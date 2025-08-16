import { No, Problema, estadosRomenia } from './estadoRomenia.js';
import { BuscaProfundidade } from './buscaProfundidade.js';

let no_arad = new No('Arad', 0, null, null);

let problemaRomenia = new Problema(
    no_arad,
    no => no.estado === 'Bucharest',
    estadosRomenia
);

console.log("DFS criada, iniciando busca...");

let dfs = new BuscaProfundidade(problemaRomenia);

// Executando passo a passo
dfs.passoBusca(); // passo 1
dfs.passoBusca(); // passo 2
dfs.passoBusca(); // passo 3
// ... continue chamando passoBusca() quantas vezes quiser

console.log("Fronteira atual:", dfs.mostraFronteira());
console.log("Solução parcial:", dfs.mostraSolucao());
