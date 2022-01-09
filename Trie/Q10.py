"""
386.
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
You must write an algorithm that runs in O(n) time and uses O(1) extra space.
"""
from collections import defaultdict

class TrieNode:

    def __init__(self, name):
        self.name = name
        self.children = [ None ] * 10
        self.isEndNode = False

class Trie:

    def __init__(self):

        self.root = self.getTrieNode("")


    def getTrieNode(self, name):

        newNode = TrieNode(name)
        newNode.children = [ None ] * 10
        newNode.isEndNode = False
        return newNode

    def insert(self, num):

        curr = self.root

        for n in str(num):
            if not curr.children[int(n)]:
                curr.children[int(n)] = self.getTrieNode(int(n))
            curr = curr.children[int(n)]

        curr.isEndNode = True

    def search(self, num):

        curr = self.root

        for n in str(num):
            if  not curr.children[int(n)]:
                return False
            curr = curr.children[int(n)]

        return curr.isEndNode


class Solution:

    def lexicalOrder(self, n):

        '''
        :param n:
        :return:
        '''

        trie = Trie()

        for i in range( 1, n+1, 1 ):

            trie.insert(i)
        # Big O(n)) time | O(n)) space.

        dfs = [ [ 0, trie.root ] ]

        res = []
        while dfs:
            curr_val, curr_node = dfs.pop()
            new_val = 10 * curr_val + int(curr_node.name) if type(curr_node.name) == int else 0

            if curr_node.isEndNode:
                res.append(new_val)

            for i in range(9, -1, -1):
                if curr_node.children[i]:
                    dfs.append( [ new_val, curr_node.children[i]] )

        return res



if __name__ == "__main__":

    sol = Solution()
    print( sol.lexicalOrder(13) )
    print(sol.lexicalOrder(2))
    # sol = Solution()
    # so
    # sol.lexicalOrder()