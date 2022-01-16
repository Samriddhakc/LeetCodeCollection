# Prim's Algorithm.
# Cut in a graph = edges/"cut" connecting visited vs unvisited set of nodes.
# Min-Cut in a graph.minimum of the cut.
# Minimum Spanning Tree. minimum of the edges requried to cover the entire set.
# Naive Prim's Algo implementation.
# Optimized Prim's Algo implementation with Min-Heap.

from collections import defaultdict
import heapq

class Graph:

    def __init__(self, n_vert):

        self.n_vert = n_vert
        self.graph = defaultdict(list)
        self.cost = defaultdict(int)

    def addEdge(self, u, v, cost):

        self.graph[u].append(v)
        self.cost[ ( u, v ) ] = cost
        self.cost[ ( v ,u ) ] = cost



    def findMSTOptimized(self):

        # O(ELogV) time | O(V) space.

        mst_set = [False] * self.n_vert
        key = [float('inf')] * self.n_vert
        parent = [-1] * self.n_vert
        key[0] = 0

        hp = [ ( 0, 0 ) ]
        while hp:
            weight, u = heapq.heappop(hp)
            mst_set[u] = True
            for v in self.graph[u]:
                if not mst_set[v] and self.cost[(u,v)] < key[v]:
                    key[v] = self.cost[(u, v)]
                    heapq.heappush( hp, ( key[v], v ) )
                    parent[v] = u

        print(parent)
        for j in range(1, len(parent)):
            if parent[j] != -1:
                print(parent[j], "--", j, " weight : ", self.cost[(j, parent[j])])

    def findMST(self):

        #O(V^2) time | O(V) space.
        # Algo.
        # Initialize a key list and initialize 0 for the initial node and infinity for all other nodes.
        # Initialize a visited set to keep track of visited vertices.
        # While len(visited) != n, find the min cut vertex. add it to the visited vertex.
        # For all the neighbors, if they are not in visited, update key based on the min_val.

        def minKey( key, mst_set ):

            # Method to find the minimum key not in the visited set.

            '''
            :param key:
            :param mst_set:
            :return:
            '''

            min = float('inf')
            min_idx = 0
            for i in range(len(mst_set)):
                if mst_set[i]  == False and key[i] < min:
                    min_idx = i
                    min = key[i]

            return min_idx

        mst_set = [ False ] * self.n_vert
        key = [ float('inf') ] * self.n_vert
        parent = [ -1 ] * self.n_vert

        key[0] = 0

        for i in range(self.n_vert):

            # Find minimum cut between visited and not visited set
            u = minKey( key, mst_set )
            mst_set[u] = True # Mark the current node in mincut as true
            for v in self.graph[u]:
                if not mst_set[v] and self.cost[(u,v)] < key[v]:
                    key[v] =  self.cost[(u,v)]
                    parent[v] = u  # This will store the minimum for sure and will be chosen at some point. # Greedy approaches fixes this.

        print(parent)
        for j in range(1, len(parent)):
            if parent[j] != -1:
                print( parent[j], "--",  j , " weight : " , self.cost[(j, parent[j])] )


if __name__ == "__main__":

    g = Graph(3)
    g.addEdge(0, 1, 1)
    g.addEdge(0, 2, 2)
    g.addEdge(1, 2, 100)
    print(g.graph)
    g.findMST()
    g.findMSTOptimized()










