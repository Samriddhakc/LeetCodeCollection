'''
1804.
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.
void erase(String word) Erases the string word from the trie
'''

class TrieNode:

    def __init__( self, val ):

        self.val = val
        self.count = 1 # how many times this prefix or word has repeated
        self.children = [ None ] * 26
        self.isEndNode = False

    def getIndex( self, let ):

        return ord(let) - ord('a')

class Trie:

    def __init__( self ):
        self.root = TrieNode("")

    def insert( self, word ):

        '''
        :param word:
        :return:
        '''

        # Big O( len(word) ) time | O( 26 * len(word) ) extra space.

        # curr to find traverse through the "trie" to find the word if it doesn't exist already
        curr = self.root

        for w in word:

            # if the node for the letter doesn't exist, initialize before moving forward
            if  not curr.children[ curr.getIndex(w) ] :

                curr.children[ curr.getIndex(w) ] = TrieNode(w)

            # increase pointer to traverse down the trie
            curr = curr.children[ curr.getIndex(w) ]

        if curr.isEndNode:
            # If, the word was already in the trie, increase the count.
            curr.count += 1

        # Mark the end of word
        curr.isEndNode = True

    def countWordsEqualTo( self, word ):

        '''
        :param word:
        :return:
        '''

        # Big O. O(len(word)) time | O(1) extra space

        # Pointer to traverse through the trie check availability of word
        curr = self.root

        for w in word:

            # If w doesn't exist in the prefix, tree, the word doesn't exist
            if not curr.children[ curr.getIndex(w) ]:
                return 0

            curr = curr.children[ curr.getIndex(w) ]

        # This takes care of the case if the word is just a prefix as well as this is initalized to 0 .
        if not curr.isEndNode:
            return 0

        return curr.count



    def countWordsStartingWith( self, prefix ):

        '''
        :param prefix:
        :return:
        '''

        # Big O.
        # O(len(T)) T is all the words starting with the prefix... size of the trie with end of prefix a sa node.
        # P(len(T)) extra space to store stack trace for dfs.

        # by making the prefix end node as the root, use dfs to find the all end nodes and sum their counts

        curr = self.root

        for p in prefix:

            # If some part of prefix is not in the trie, there will be no words starting with the prefix.
            if not curr.children[ curr.getIndex(p) ]:
                return 0

            curr = curr.children[ curr.getIndex(p) ]

        dfs, count = [ curr ], 0

        while dfs:

            # pop the current node
            curr_node = dfs.pop()

            # if it is the ending node, increase by the count of occurence
            if curr_node.isEndNode:

                count += curr_node.count

            # add the non-null children
            for i in range(26):
                if curr_node.children[i]:
                    dfs.append( curr_node.children[i] )

        return count


    def erase( self, word ):

        # iterate through the word in trie. if the word as isEndWord or none null children, move forward.
        # mark end of curr word as isEndNode = False.
        # if this node has children, done here.
        # If not, retraverse and delete all nodes that doesn't have any children.

        # O(len(word)) time | O(len(word)) extra space 
        # urr to iterate through the trie
        curr = self.root

        # keep track of parent nodes in the trie
        p_stack = []

        for w in word:

            # w exists in the children for trie, move forward and track the parent
            if curr.children[curr.getIndex(w)]:
                p_stack.append(curr)
                curr = curr.children[curr.getIndex(w)]
            else: # else, the word to be deleted is not present
                return

        curr.count -= 1 # decrease count for the word
        if curr.count == 0: # if this is 0, if no children present, start deleting nodes in parent that can be
                            # cleared, i.e. has it has the only parent

            if (curr.children.count(None) == 26):
                while p_stack:
                    curr_node = p_stack.pop()
                    if (curr_node.children.count(None) == 25
                            and not curr_node.isEndNode):
                        curr_node.children = [None] * 26
                    else:
                        break
                # else:
                #     curr.isEndNode = False
                    # Should not we consider for the case where child exists for
            # the word but only the word is deleted?




if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("apple")
    trie.insert("apple")
    trie.insert("app")
    trie.insert("apple")
    trie.insert("apple")
    trie.insert("app")
    trie.insert("apple")
    trie.insert("app")

    print(trie.countWordsEqualTo("apple"))

