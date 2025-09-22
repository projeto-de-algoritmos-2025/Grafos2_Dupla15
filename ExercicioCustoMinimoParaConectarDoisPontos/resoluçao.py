import heapq

class Solution:

    def minCostConnectPoints(self, points):
        """
        Calcula o custo mínimo para conectar todos os pontos usando o Algoritmo de Prim.
        """
        N = len(points)
        if N <= 1:
            return 0

        # Um conjunto para acompanhar os vértices já incluídos na MST.

        visited = set()

        # Uma min-heap para armazenar as arestas potenciais.
        # Cada elemento é uma tupla: (custo, índice_do_ponto).

        min_heap = [(0, 0)]  #Comece com o ponto 0 com um custo de 0.


        total_cost = 0
        edges_used = 0

        # O loop continua até termos N-1 arestas em nossa MST, conectando todos os N pontos.

        while min_heap and edges_used < N:
            # pega a aresta com o menor peso
            cost, u_idx = heapq.heappop(min_heap)

            #Se esse ponto ja esta na MST, puls
            if u_idx in visited:
                continue

            # Adiciona o ponto no mst
            visited.add(u_idx)
            total_cost += cost
            edges_used += 1

            # pega as coordenadas do atual ponto U
            ux, uy = points[u_idx]

            # agora considera todas as conexoes partindo do ponto U
            # para outros pontos V, ainda  nao estarao na MST
            for v_idx in range(N):
                if v_idx not in visited:
                    # obtem as coordenadas do proximo ponto v
                    vx, vy = points[v_idx]
                    
                    # Calcula distancia de manhattan
                    manhattan_distance = abs(ux - vx) + abs(uy - vy)
                    
                    # Adiciona nova aresta ao heap 
                    heapq.heappush(min_heap, (manhattan_distance, v_idx))
        
        return total_cost

# Exemplo de uso:
solver = Solution()

# Exemplo 1
points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(f"Input: {points1}")
print(f"Output: {solver.minCostConnectPoints(points1)}") # Esperado: 20

print("-" * 20)

# Exemplo 2
points2 = [[3,12],[-2,5],[-4,1]]
print(f"Input: {points2}")
print(f"Output: {solver.minCostConnectPoints(points2)}") # Esperado: 18

print("-" * 20)

# Exemplo 3
points3 = [[0,0]]
print(f"Input: {points3}")
print(f"Output: {solver.minCostConnectPoints(points3)}") # Esperado: 0



