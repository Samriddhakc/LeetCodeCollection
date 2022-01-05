"""
Q2. 1268. Search Suggestions System
You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed.
"""

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

#  m
# is isPrefix(), then use dfs to find the first three matching words.
#
#
from Trie import Trie

class Solution:

    def dfs( self, head_node, prefix ):

        #O(V+E) time => O( len(products) * 3 ) time

        stack = [ [prefix, head_node ] ]
        result = []
        while stack:
            curr_prefix, curr_node = stack.pop()
            if curr_node.isEndNode:
                result.append(curr_prefix)

            for child_idx in range( 25, -1, -1 ):
                if curr_node.children[child_idx]:
                    child_node = curr_node.children[child_idx]
                    stack.append( [ curr_prefix + chr(97 + child_idx) , child_node] )
            if len(result) == 3:
                return result
        return result


    def suggestedProducts(self, products, searchWord ):

        '''
        :param products:
        :param searchWord:
        :return:
        '''

        trie = Trie()

        for word in products:
            trie.insert(word)

        prefix = ""
        result = []
        p_crawl = trie.root

        prefix = ""

        # O ( len(searchWord)^2 * len(products) * 26 * len(max(products)) ) time
        # O( len(max(products)) * 26 * len(products) ) space

        for s in searchWord:
            prefix += s
            curr_result = []
            p_crawl = p_crawl.children[trie.getIndex(s)]
            if p_crawl:
                curr_result = self.dfs( p_crawl, prefix )
            result.append(curr_result)
        return result



if __name__ == "__main__":
    sol = Solution()
    print( sol.suggestedProducts( ["mobile","mouse","moneypot","monitor","mousepad"], "mouse" ) )
