

# Find minimum path from source to target.
# optimize, d(v) <= d(v) + d(u, v), then update d(v), where u is in visited set, v is not in visited set.

from collections import defaultdict
import heapq

class Graph:

    def __init__(self, n_vert):

        self.n_vert = n_vert
        self.graph = defaultdict(list)
        self.cost = defaultdict(int)

    def addEdge(self, u, v, w):

        self.graph[u].append(v)
        self.graph[v].append(u)
        self.cost[(u, v)] = w
        self.cost[(v, u)] = w


    def findMinVert(self, d, visited):

        min_key = -1
        min_val = float('inf')
        for i in range(len(d)):
            if i not in visited and d[i] < min_val:
                min_key = i
                min_val = min_key

        return min_key


    def DikjstraMinCostPathOptimized(self, source, target):

        visited = set()
        d = [ float('inf') ] * self.n_vert
        d[source] = 0
        hp = [ [ 0, source] ]

        # O(ELogV) time | O(V) space

        while hp:

            d_val, min_vert = heapq.heappop(hp)
            visited.add(min_vert)
            if min_vert == target:
                break
            for n_v in self.graph[min_vert]:
                if n_v not in visited and (d_val + self.cost[(min_vert, n_v)]) < d[n_v]:
                    d[n_v] = d_val + self.cost[(min_vert, n_v)]
                    heapq.heappush( hp, ( d[n_v], n_v ) )


        return d[target] if 0 <= target < self.n_vert else float('inf')


    def DikjstraMinCostPath(self, source, target):

        '''
        :param source: source vertex.
        :param target: target vertex
        :return: Minimum cost traverseing from source to target.
        '''

        # O( V * (V+E) ) time | O(V+E) space.

        visited = set() # track all visited nodes.
        d = [ float('inf') ] * self.n_vert
        d[source] = 0

        cost = 0

        for i in range(self.n_vert):

            min_vert = self.findMinVert( d, visited)
            visited.add(min_vert)
            if target == min_vert:
                break

            for n_v in self.graph[min_vert]:
                if n_v not in visited and ( d[min_vert] + self.cost[(min_vert, n_v)]  ) < d[n_v]:
                    d[n_v] = d[min_vert] + self.cost[(min_vert, n_v)]

        return d[target] if 0 <= target < self.n_vert else float('inf')


if __name__ == "__main__":

    g = Graph(2)
    g.addEdge(0, 1, 1)
    assert( g.DikjstraMinCostPath(0, 1) == 1)

    g = Graph(3)
    g.addEdge(0, 1, 1)
    g.addEdge(1, 2, 100)
    g.addEdge(0, 2, 3)
    assert(g.DikjstraMinCostPath(0, 1) == 1)
    assert(g.DikjstraMinCostPath(0, 100) == float('inf') )
    assert(g.DikjstraMinCostPath(1, 2) == 4)
    assert(g.DikjstraMinCostPath(1, -200) == float('inf') )

    g = Graph(2)
    g.addEdge(0, 1, 1)
    assert (g.DikjstraMinCostPathOptimized(0, 1) == 1)

    g = Graph(3)
    g.addEdge(0, 1, 1)
    g.addEdge(1, 2, 100)
    g.addEdge(0, 2, 3)
    assert (g.DikjstraMinCostPathOptimized(0, 1) == 1)
    assert (g.DikjstraMinCostPathOptimized(0, 100) == float('inf'))
    assert (g.DikjstraMinCostPathOptimized(1, 2) == 4)
    assert (g.DikjstraMinCostPathOptimized(1, -200) == float('inf'))








