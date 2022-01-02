"""
Q7. Find K-Length Substrings With No Repeated Characters
Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.
"""

from collections import Counter

class Solution:

    def numKLenSubstrNoRepeats(self, s, k):

        countSubStrs = Counter(s[:k])

        #abcb
        # || hek len of key paris with difference of indices.

        numSubstrs = 1 if  len(countSubStrs)  == k else 0

        for up in range( k, len(s) ):
            left_str = s[up - k]
            countSubStrs[left_str] -= 1
            if countSubStrs[left_str] == 0:
                countSubStrs.pop(left_str)
            countSubStrs[s[up]] += 1
            numSubstrs += 1 if len(countSubStrs) == k else 0
        return numSubstrs



if __name__ == "__main__":
    sol = Solution()
    print(sol.numKLenSubstrNoRepeats("havefunonleetcode", 5))
