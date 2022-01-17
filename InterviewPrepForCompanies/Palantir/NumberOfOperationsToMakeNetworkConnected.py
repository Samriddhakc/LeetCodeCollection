from collections import defaultdict
from collections import defaultdict


class Node:

    def __init__(self, parent):
        self.parent = parent
        self.rank = 0


def union(nodes, x, y):
    if nodes[x].rank > nodes[y].rank:
        nodes[y].parent = x
        nodes[x].rank += 1

    if nodes[y].rank > nodes[x].rank:

        nodes[x].parent = y
        nodes[y].rank += 1

    else:

        nodes[y].parent = x
        nodes[x].rank += 1


def find(nodes, x):
    if nodes[x].parent != x:
        nodes[x].parent = find(nodes, nodes[x].parent)

    return nodes[x].parent


class Solution:

    def makeConnected(self, n, connections):

        if n <= 1:  # Def of connections not well defined.
            return 0

        if len(connections) < (n - 1):  # A disconnected set without a minimum spanning tree.
            return -1

        # Disjoint set algo
        num_disjoint = set()
        nodes = [Node(i) for i in range(n)]

        # Union the parent sets/join them before counting.
        # O ( len(connections) * lgV )  time | O(V) rpcie
        for conn in connections:
            union(nodes, find(nodes, conn[0]), find(nodes, conn[1]))

        for comp in range(n):
            num_disjoint.add(find(nodes, comp))

        return len(num_disjoint) - 1


if __name__ == "__main__":

    sol = Solution()
    assert( sol.makeConnected( 0, [] ) == 0 )
    assert( sol.makeConnected( 1, [] ) == 0 )
    #Consider the case where len(connections) < (n - 1): # This is not possible/return -1
    assert( sol.makeConnected( 3, [ [0, 1], [0, 2], [1,2] ]  ) == 0 )
    assert ( sol.makeConnected(4, [ [0, 1], [0, 2], [1,2] ]  )  == 1 )
    assert ( sol.makeConnected( 6, [[0,1],[0,2],[0,3],[1,2],[1,3]] ) == 2 )
    assert ( sol.makeConnected(6, [ [0,1],[0,2],[0,3],[1,2] ]) == -1 )

    # 0 1 2 3 4
    # 0 0 0 3 3
