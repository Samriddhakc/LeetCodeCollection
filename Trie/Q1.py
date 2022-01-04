"""
Q1. 1065. Index Pairs of a String
Given a string text and an array of strings words, return an array of all index pairs [i, j] so that the substring text[i...j] is in words.
Return the pairs [i, j] in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate).
"""
from Trie import Trie
class Solution:

    def indexPairs(self, text,  words):

        '''
        :param text:
        :param words:
        :return:
        '''

        # ans = []
        # for i in range(len(text)):
        #     for j in range(i + 1, len(text) + 1):
        #         if text[i:j] in set(words):
        #             ans.append([i, j - 1])
        # return ans
        # O(N^3) time | O(N)space | O(1) extra space

        # O(N^2) time | O(len(words) * 26 * max(word) ) space.

        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = []
        for i in range(len(text)):
            curr_node = trie.root
            for j in range(i, len(text)):
                curr_node = curr_node.children[trie.getIndex(text[j])]
                if not curr_node:
                    break
                if curr_node.isEndNode:
                    ans.append([i, j])

        return ans






if __name__ == "__main__":
    sol = Solution()
    print ( sol.indexPairs("thestoryofleetcodeandme",  ["story","fleet","leetcode"]) )