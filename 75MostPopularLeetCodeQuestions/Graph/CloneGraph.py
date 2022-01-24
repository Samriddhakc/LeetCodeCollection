"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hash_node_copy = {}
        if not node:
            return None

        root_val = node.val
        dfs = [node]
        visited = set([node])
        while dfs:
            curr_node = dfs.pop()
            # if node has already been copied, just retrieve that from a hash lookup
            if curr_node in hash_node_copy:
                new_node_copy = hash_node_copy[curr_node]
            # else create a new node and put it in the hash table
            else:
                new_node_copy = Node(curr_node.val)
                hash_node_copy[curr_node] = new_node_copy

            # go through each neigh in the neighbors
            for neigh in curr_node.neighbors:
                if neigh in hash_node_copy:
                    new_node_copy.neighbors.append(hash_node_copy[neigh])
                else:
                    neigh_copy = Node(neigh.val)
                    hash_node_copy[neigh] = neigh_copy
                    new_node_copy.neighbors.append(neigh_copy)

                if neigh not in visited:
                    dfs.append(neigh)
                    visited.add(neigh)

        return hash_node_copy[node]
