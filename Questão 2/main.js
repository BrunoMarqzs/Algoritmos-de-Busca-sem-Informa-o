console.log("Arquivo main.js iniciado");

import { No, Problema, estadosRomenia } from './estadoRomenia.js';
import { BuscaProfundidade } from './buscaProfundidade.js';

console.log("Imports carregados");

// nó inicial e problema
let no_arad = new No('Arad', 0, null, null);
let problemaRomenia = new Problema(no_arad, no => no.estado === 'Bucharest', estadosRomenia);

let dfs = new BuscaProfundidade(problemaRomenia);
console.log("DFS criada, iniciando busca...");
dfs.efetuarBusca();
