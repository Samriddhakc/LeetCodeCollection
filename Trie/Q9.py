"""
Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.
A query word queries[i] matches pattern if you can insert lowercase English letters pattern so that it equals the query. You may insert each character at any position
and you may not insert any characters.
"""

class Solution:

    def matchPattern( self, str1, pattern ):
        # O(len(str1)) time
        if len(pattern) > len(str1):

            return False

        p1, p2 = 0, 0

        while ( p1 < len(str1) ):

            #  if str1, and pattern element matches, move the pointer for both pattern and str forward
            if p2 < len(pattern) and str1[p1] == pattern[p2]: # if
                    p2 += 1
            # If it is a capital letter, and not a match in Pattern, break here.
            elif str1[p1].isupper():
                return False
            p1 += 1
        return p2 == len(pattern) # return true if matches all the pattern else return false






    def camelMatch(self, queries, pattern):

        '''
        :param queries:
        :param pattern:
        :return:
        '''
        result = []
        # O( len(queries) * len(max(queries)) time
        # O(len(queries)) space
        for query in queries:
            result.append(self.matchPattern(query, pattern))

        return result


if __name__ == "__main__":
    sol = Solution()
    print( sol.camelMatch ( ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB" ) )






