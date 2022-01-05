"""
1233. Remove Sub-Folders from the Filesystem
Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.
If a folder[i] is located within another folder[j], it is called a sub-folder of it.
The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.
For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
"""
import copy


class TrieNode:

    def __init__(self, val):
        self.val = val
        self.children = [ None ] * 27 # [a-z] from 0...25, 26 for the char '/'
        self.isEndOfWord = False # This is a loosely coupled word. In this case, it would mean isAFolder?

class Trie:

    def __init__(self):

        self.root = self.getTrieNode("?")


    def getTrieNode(self, val):

        new_node = TrieNode(val)
        new_node.children = [ None ] * 27
        self.isEndOfWord = False
        return new_node

    def getIndex(self, letter):

        return ord(letter) - 97

    def insert(self, val):
        p_crawl = self.root
        for s in val:
            child_idx = self.getIndex(s) if s.isalpha() else 26
            if not p_crawl.children[child_idx]:
                p_crawl.children[child_idx] = self.getTrieNode(s)
            p_crawl = p_crawl.children[child_idx]
        p_crawl.isEndOfWord=True

    def search(self, val):
        p_crawl = self.root
        for s in val:
            if not p_crawl.children[self.getIndex(s)]:
                return False
            p_crawl = p_crawl.children[self.getIndex(s)]
        return p_crawl.isEndOfWord



class Solution:

    def removeSubFolders(self, folders):

        '''
        :param folders:
        :return:
        '''

        #Idea.
        #       X
        #     /  \
        #    a*    c
        #   /     / \
        #  b*    f*  d*
        #              \
        #               e*
        # ["/a", "/c/f", "/c/d" ]
        # Algorithm.
        # Turn folder into a string without /.
        # Initialize a trie and populate with the length of the folder.
        # Use a variation of dfs with the trie. If endOfWord or IsFolder, stop and extract => convert into into folder.
        # Done.
        # O( len(folder) * len(max(folder)) ) time
        # O( len(folder) *  len(max(folder)) * 27  ) time
        # O(len(folder)) time
        # O ( len(folder) * 26 * 100 ) space.
        
        trie = Trie()
        for fold in folders:
            trie.insert( fold )

        dfs = [ [ "/", trie.root ] ]
        result = []
        while dfs:
            folder_str, curr_node = dfs.pop()
            folder_str += curr_node.val
            if curr_node.isEndOfWord:
                result.append(folder_str[2:])
                for child_idx in range(26):
                    if curr_node.children[child_idx]:
                        dfs.append([copy.deepcopy(folder_str), curr_node.children[child_idx]])
            else:
                for child_idx in range(27):
                    if curr_node.children[child_idx]:
                        dfs.append([ copy.deepcopy(folder_str), curr_node.children[child_idx]])
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeSubFolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
    print(sol.removeSubFolders( ["/a","/a/b/c","/a/b/d"]))
    print(sol.removeSubFolders( ["/ac","/a"]))


    #         /
    #       /  \
    #      a    b
    #     / \  / \
    #    c
    #