"""
Q16.Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""

class Solution:

    def maxVowels(self, s, k):

        '''
        :param s:
        :param k:
        :return:
        '''
        vowels = { 'a', 'e', 'i', 'o', 'u' }
        num_vowels = len( [ x for x in s[:k] if x in vowels] )
        max_vowels = num_vowels

        for idx in range( k, len(s) ):
            num_vowels -= 1 if s[idx] in vowels else 0
            num_vowels += 1 if s[idx] in vowels else 0
            max_vowels = max( max_vowels, num_vowels )

        return max_vowels

if __name__ == "__main__":
    sol = Solution()
