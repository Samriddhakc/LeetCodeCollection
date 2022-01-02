"""
Q11.
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c
"""

from collections import defaultdict

class Solution:

    def numberOfSubstrings(self, s):

        '''
        :param s:
        :return:
        '''

        char_hash = defaultdict(int)
        left = 0
        num_substr = 0
        for right in range(len(s)):
            char_hash[s[right]] += 1
            while (len(char_hash) == 3):
                num_substr += len(s) - right
                char_hash[s[left]] -= 1
                if char_hash[s[left]] == 0:
                    char_hash.pop(s[left])
                left += 1
        return num_substr


if __name__ == "__main__":
    sol = Solution()
    sol.numberOfSubstrings()