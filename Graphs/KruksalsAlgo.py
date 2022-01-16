# Using union find by rank to detect cycle.

from collections import defaultdict

class Node:

    def __init__(self, parent):
        self.parent = parent
        self.rank = 0

class Graph:

    def __init__(self, n_vert ):

        self.n_vert = n_vert
        self.graph = []

    def union(self, nodes, x, y):

        if nodes[x].rank < nodes[y].rank:

            nodes[x].parent = y
            nodes[y].rank += 1

        if nodes[x].rank > nodes[y].rank:

            nodes[y].parent = x
            nodes[x].rank += 1

        else:

            nodes[y].parent = x
            nodes[x].rank += 1


    def find(self, nodes, x):

        if nodes[x].parent != x:

            nodes[x].parent = self.find(nodes, nodes[x].parent)

        return nodes[x].parent

    def addEdge(self, x, y, w):
        self.graph.append( [ x, y, w] )

    def kruksalsMinSpanTree(self):

        # sort edges
        self.graph.sort( key=lambda x: x[2] ) #sort by edge weights

        nodes = [ Node(i) for i in range(self.n_vert) ]
        count = 0
        parent = [ 0 ] * self.n_vert

        # O(ELogV + ELogE)= E can be at most V^2 in a complete graph = O(ElogV) or O(ElogE).

        for edge in self.graph:

            rep_1 = self.find( nodes, edge[0] )
            rep_2 = self.find( nodes, edge[1] )

            if rep_1 == rep_2:
                break

            parent[edge[0]] = edge[1]
            self.union( nodes, edge[0], edge[1] )
            count += 1

        if count == (self.n_vert - 1):
            for idx in range(len(parent)):
                print(idx, "--", parent[idx] )
            print("--")
        else:
            print("MST Not possible!")
        return parent


if __name__ == "__main__":
    graph = Graph(2)
    graph.addEdge(0, 1, 2)
    graph.kruksalsMinSpanTree()

    graph2 = Graph(3)
    graph2.addEdge(0, 1, 1)
    graph2.addEdge(0, 2, 2)
    graph2.addEdge(1, 2, 1)
    graph2.kruksalsMinSpanTree()







