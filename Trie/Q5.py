"""
1698. Number of Distinct Substrings in a String
Given a string s, return the number of distinct substrings of s.
A substring of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and
any number (possibly zero) from the back of the string.
"""

from Trie import Trie

class Solution:

    def countDistinct(self, s):

        '''
        :param s:
        :return:
        '''

        # Brute force algo
        # total = set()
        # # O(N^3) time. O(N) space. N = len(s)
        # for idx in range(len(s)):
        #     for idx_2 in range(idx + 1, len(s) + 1):
        #         total.add(s[idx: idx_2])
        # return len(total)
        # O(N^2) time | O( N * 26 * N^2) space.
        # unique = 0
        # for i in range(len(s)):
        #     trie = d
        #     for j in range(i, len(s)):
        #         if not s[j] in trie:
        #             trie[s[j]] = {}
        #             # trie[s[j]] = { 'end': True }
        #             # if  trie[s[j]]['end']:
        #             unique += 1
        #             # trie[s[j]]['end'] = False
        #         trie = trie[s[j]]
        # return unique
        trie = Trie()
        unique = 0
        root = trie.root
        for i in range(len(s)):
            p = root
            for j in range(i, len(s)):
                if not p.children[trie.getIndex(s[j])]:
                    p.children[trie.getIndex(s[j])] = trie.getTrieNode(s[j])
                    unique += 1
                p = p.children[trie.getIndex(s[j])]
        return unique

        # aab
        #     X
        #    / \
        #    a
        #    |
        #    a
        #    |
        #    b



if __name__ == "__main__":
    sol = Solution()
    print(sol.countDistinct("a"))
    print(sol.countDistinct("ab"))
    print(sol.countDistinct("aab")) # a, aa, aab, ab, b,