"""
648. Replace Words
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".
Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.
Return the sentence after the replacement.
"""

from Trie import Trie

class Solution:

    def replaceWords(self, dictionary, sentence):

        '''
        :param dictionary:
        :return:
        '''

        lis = sentence.split(" ")
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        # O(len(sentence)) time | O(26 * len(dictionary))  + O(len(sentence)) space.

        for idx, word in enumerate(
                sentence.split(" ")):
            root = trie.root
            result = []
            for w in word:
                if root and root.children[trie.getIndex(w)]:
                    if root.children[trie.getIndex(w)].isEndNode:
                        result.append(w)
                        break
                    root = root.children[trie.getIndex(w)]
                else:
                    root = None
                result.append(w)
            lis[idx] = "".join(result)
        return " ".join(lis)

        # O(N * w^2 ) time. O(N) soace n - kength of the sentence.

        # for idx, word in enumerate(sentence.split(" ")):
        #     #root = trie.root
        #     s =  ""
        #     for w in word:
        #         s += w
        #         if s in set(dictionary):
        #             sentence[idx] = s
        #             break
        #         # if not root.search(w):
        #         #
        #         #     break




if __name__ == "__main__":
    sol = Solution()
    print(sol.replaceWords( ["cat","bat","rat"], "the cattle was rattled by the battery"))
