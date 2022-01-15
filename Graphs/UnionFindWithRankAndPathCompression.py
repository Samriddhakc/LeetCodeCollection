from collections import defaultdict

class Node:

    def __init__( self, val ):

        self.parent = val
        self.rank = 0

class Graph:

    def __init__( self, n_verices ):

        self.n_vertices = n_verices
        self.graph = defaultdict(list)

    def addEdge( self, u, v ):

        self.graph[u].append(v)

    def union( self, vert_nodes,  x, y ):

        '''Union by Rank. Helps to form a balanced binary tree. '''

        if vert_nodes[x].rank > vert_nodes[y].rank:
            vert_nodes[y].parent = x

        if vert_nodes[x].rank < vert_nodes[y].rank:
            vert_nodes[x].parent = y

        else:
            vert_nodes[y].parent = x
            vert_nodes[x].rank += 1

    def find( self, vertex_nodes, idx ):

        '''Path Compression for Union Find.'''

        if vertex_nodes[idx].parent != idx:

            vertex_nodes[idx].parent = self.find( vertex_nodes, vertex_nodes[idx].parent )

        return vertex_nodes[idx].parent




    def detectIsCyclic(self):

        # O(VLGV) time | O(V) space.

        vert_nodes = [ Node(x) for x in range( self.n_vertices ) ]

        for u in self.graph:
            for v in self.graph[u]:

               p1 = self.find(vert_nodes, u)
               p2 = self.find(vert_nodes, v)
               if p1 == p2:
                   return True
               self.union(vert_nodes, u, v)

        return False


if __name__ =="__main__":

    g = Graph(2)
    g.addEdge(1, 0)
    assert (g.detectIsCyclic() == False)
    g.addEdge(0, 1)
    assert (g.detectIsCyclic() == True)

    g2 = Graph(3)
    g2.addEdge(0, 1)
    assert (g2.detectIsCyclic() == False)
    g2.addEdge(1, 2)
    assert (g2.detectIsCyclic() == False)
    # g2.addEdge(2, 0)
    # assert (g2.detectIsCyclic() == True)

    # 0 1 2
    # 0 1 2

    # 0 1 2                 #
    #                       #       0
    # 0 1 2                 #      / \
                            #     1   2






