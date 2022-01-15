
# Adjacency list representation for graph


# Matrix represnetation for graph

from collections import defaultdict

class Graph:

    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
                                            #  1    2    3
        self.graph[u].append(v)             # -1   -1   -1

    def find(self, parent, i):

        # If the vertex is represnetation of the set, return the idx.
        if parent[i] == -1:
            return i

        # Else, find the representation of i
        return self.find(parent, parent[i])


    def union(self, parent, x, y):

        parent[y] = x

    def detectIsCyclic(self):
        # O( (V + E) * V )= O(N^2) time | O(N^2) space
        parent = [ -1 ] * self.n_vertices

        for u in range(self.n_vertices):
            for v in self.graph[u]:
                p1 = self.find(parent, u)
                p2 = self.find(parent, v)
                if p1 == p2:
                    return True
                self.union(parent, p1, p2)
        return False


if __name__ == "__main__":

    g = Graph(2)
    g.addEdge(0, 1)
    assert(g.detectIsCyclic() == False)
    g.addEdge(1,0)
    assert(g.detectIsCyclic() == True)

    g2 = Graph(3)
    g2.addEdge(0, 1)
    assert(g2.detectIsCyclic() == False)
    g2.addEdge(1, 2)
    assert(g2.detectIsCyclic() == False)
    g2.addEdge(2, 0)
    assert(g2.detectIsCyclic() == True)

