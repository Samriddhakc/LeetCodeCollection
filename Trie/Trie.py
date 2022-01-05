
class TrieNode:

    def __init__(self, val):
        self.val = val
        self.children = [ None ] * 26
        self.isEndNode = False

class Trie:

    def __init__(self):
        self.root = self.getTrieNode("X")

    def getTrieNode(self, newVal):

        '''
        :param newVal:
        :return:
        '''

        newNode = TrieNode(newVal)
        newNode.children =  [ None ] * 26
        return newNode

    def getIndex(self, alpha):
        return ord(alpha) - ord('a')

    def insert(self, str_val ):

        '''
        :param newVal:
        :return:
        '''
        #      X
        #    /  \
        #   a
        #  / \
        # b   c

        # O(M) time M is the length of the key.
        # O( M * N * ALPHABEST SIZE ) space. N is all the keys.

        p_crawl = self.root
        for idx, s in enumerate(str_val):
            if not  p_crawl.children[self.getIndex(s)]:
                p_crawl.children[self.getIndex(s)] = self.getTrieNode(s)
            p_crawl = p_crawl.children[self.getIndex(s)]
        p_crawl.isEndNode = True


    def search(self, str_val ):

        p_crawl = self.root

        for s in str_val:
            if not p_crawl.children[self.getIndex(s)]:
                return False
            p_crawl = p_crawl.children[self.getIndex(s)]

        return p_crawl.isEndNode

    def isPrefix(self, pref):

        p_crawl = self.root

        for p in pref:
            if not p_crawl.children[self.getIndex(p)]:
                return None, False
            p_crawl = p_crawl.children[self.getIndex(p)]

        return p_crawl, True



if __name__ == "__main__":
    trie_ex = Trie()
    trie_ex.insert("ab")
    trie_ex.insert("ac")
    print(trie_ex.search("ab"))
    print(trie_ex.search("ac"))
    print(trie_ex.search("a"))
    trie_ex.insert("avc")
    print(trie_ex.search("avc"))


