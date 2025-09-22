1489. Encontrar Arestas Críticas e Pseudo-Críticas em uma Árvore Geradora Mínima
Dificuldade: Difícil

Descrição do Problema
Dado um grafo conexo, não direcionado e ponderado com n vértices numerados de 0 a n-1, e um array edges onde edges[i] = [ai, bi, weighti] representa uma aresta bidirecional e ponderada entre os nós ai e bi.

Uma árvore geradora mínima (MST - Minimum Spanning Tree) é um subconjunto das arestas do grafo que conecta todos os vértices sem ciclos e com o menor peso total possível.

Encontre todas as arestas críticas e pseudo-críticas na árvore geradora mínima do grafo dado.

Uma aresta crítica é uma aresta da MST cuja exclusão do grafo causaria um aumento no peso da MST.

Uma aresta pseudo-crítica é uma aresta que pode aparecer em algumas MSTs, mas não em todas.

Note que você pode retornar os índices das arestas em qualquer ordem.

Exemplos
Exemplo 1:
Input:

n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]

Output:

[[0,1],[2,3,4,5]]

Explicação: As arestas 0 e 1 aparecem em todas as MSTs possíveis, portanto, são arestas críticas. As arestas 2, 3, 4 e 5 fazem parte de apenas algumas MSTs, portanto, são consideradas arestas pseudo-críticas.

Exemplo 2:
Input:

n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]

Output:

[[],[0,1,2,3]]

Explicação: Como todas as 4 arestas têm peso igual, escolher quaisquer 3 das 4 arestas resultará em uma MST. Portanto, todas as 4 arestas são pseudo-críticas.

Restrições (Constraints)
2 <= n <= 100

1 <= edges.length <= min(200, n * (n - 1) / 2)

edges[i].length == 3

0 <= ai < bi < n

1 <= weighti <= 1000

Todos os pares (ai, bi) são distintos.