
"""
Given an array of strings words, find the longest string in words such that every prefix of it is also in words.
For example, let words = ["a", "app", "ap"]. The string "app" has prefixes "ap" and "a", all of which are in words.
Return the string described above. If there is more than one string with the same length, return the lexicographically smallest one, and if no string exists, return "".
"""

from Trie import Trie

class Solution:

    def longestWord(self, words):

        '''
        :param words:
        :return:
        '''

        ''' populate the trie. len(words) * max(len(word))  
            Use dfs to find the deepest branch in the trie O(len(words) ) time.
            as max(len(word)) is bounded, O(len(words)) time | O(len(words)) space'''

        trie = Trie()
        for word in words:
            trie.insert(word)

        root = trie.root
        max_prefix = ""
        stack = [[root, ""]]

        while stack:
            curr_node, prefix = stack.pop()
            if (len(max_prefix) < len(prefix)):

                max_prefix = prefix

            for i in range(25, -1, -1):
                if curr_node.children[i]:
                    if curr_node.children[i].isEndNode:
                        stack.append([curr_node.children[i], prefix + chr(97 + i)])
        return max_prefix



if __name__ == "__main__":


    '''
    execute code here. 
    '''
    sol = Solution()
    print( sol.longestWord( ["k", "ki", "kir", "kira", "kiran"] ) )
    print( sol.longestWord( ["a", "banana", "app", "appl", "ap", "apply", "apple"]) )

    print( sol.longestWord( ["ab", "bc"]) )
