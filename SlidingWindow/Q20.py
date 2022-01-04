"""
Q20. Maximum Number of Occurrences of a Substring
Given a string s, return the maximum number of ocurrences of any substring under the following rules:
The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.
"""

from collections import defaultdict

class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """

        if len(s) < minSize:
            return 0

        substring_hash = defaultdict(int)
        letter_hash = Counter(s[:minSize])

        windSize = minSize

        if len(letter_hash) <= maxLetters:
            substring_hash[s[:windSize]] = 1

        l = 0
        for r in range(windSize, len(s)):
            letter_hash[s[l]] -= 1
            if (letter_hash[s[l]] == 0):
                letter_hash.pop(s[l])
            letter_hash[s[r]] += 1
            if len(letter_hash) <= maxLetters:
                substring_hash[s[l + 1:r + 1]] += 1
            l += 1

        return max(substring_hash.values()) if substring_hash else 0


if __name__ == "__main__":

