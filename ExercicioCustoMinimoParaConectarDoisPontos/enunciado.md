1584. Custo Mínimo para Conectar Todos os Pontos

Dificuldade: Média


Descrição do Problema

Você recebe um array points que representa coordenadas inteiras de alguns pontos em um plano 2D, onde points[i] = [xi, yi].
O custo para conectar dois pontos [xi, yi] e [xj, yj] é a distância de Manhattan entre eles: |xi - xj| + |yi - yj|, onde |val| denota o valor absoluto de val.

Retorne o custo mínimo para conectar todos os pontos. Todos os pontos são considerados conectados se houver exatamente um caminho simples entre quaisquer dois pontos.
Exemplos

Exemplo 1:
Input:points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output:20

Explicação: Podemos conectar os pontos para obter um custo mínimo de 20. Note que há um caminho único entre cada par de pontos.
Exemplo 2:
Input:points = [[3,12],[-2,5],[-4,1]]
Output:18

Restrições (Constraints)


1 <= points.length <= 1000

-10^6 <= xi, yi <= 10^6

Todos os pares (xi, yi) são distintos.