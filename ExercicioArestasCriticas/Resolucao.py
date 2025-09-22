class UnionFind:
    """
    Estrutura de dados Union-Find (Disjoint Set Union) para o Algoritmo de Kruskal.
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.num_components = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            self.num_components -= 1
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        
        # 1. Adicionar o índice original a cada aresta para referência futura.
        for i, edge in enumerate(edges):
            edge.append(i)
        
        # 2. Ordenar as arestas pelo peso.
        edges.sort(key=lambda x: x[2])
        
        # 3. Calcular o peso da MST original do grafo.
        uf_base = UnionFind(n)
        original_mst_weight = 0
        for u, v, weight, _ in edges:
            if uf_base.union(u, v):
                original_mst_weight += weight
        
        critical_edges = []
        pseudo_critical_edges = []
        
        num_edges = len(edges)
        
        # 4. Iterar sobre cada aresta para classificá-la.
        for i in range(num_edges):
            
            # TESTE DE CRITICIDADE: Calcular a MST ignorando a aresta 'i'.
            uf_ignore = UnionFind(n)
            weight_ignore = 0
            for j in range(num_edges):
                if i == j:
                    continue
                u, v, weight, _ = edges[j]
                if uf_ignore.union(u, v):
                    weight_ignore += weight
            
            # Se o grafo ficou desconectado ou o peso aumentou, a aresta é crítica.
            if uf_ignore.num_components > 1 or weight_ignore > original_mst_weight:
                critical_edges.append(edges[i][3]) # Adiciona o índice original.
                continue # Uma aresta crítica não pode ser pseudo-crítica.

            # TESTE DE PSEUDO-CRITICIDADE: Calcular a MST forçando a inclusão da aresta 'i'.
            uf_force = UnionFind(n)
            u_force, v_force, weight_force, _ = edges[i]
            uf_force.union(u_force, v_force)
            weight_with_force = weight_force
            
            for j in range(num_edges):
                if i == j:
                    continue
                u, v, weight, _ = edges[j]
                if uf_force.union(u, v):
                    weight_with_force += weight
            
            # Se conseguimos o mesmo peso da MST original, a aresta é pseudo-crítica.
            if weight_with_force == original_mst_weight:
                pseudo_critical_edges.append(edges[i][3])

        return [critical_edges, pseudo_critical_edges]
