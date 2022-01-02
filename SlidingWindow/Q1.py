# Q1. Substrings of size Three with Distinct Characters
# A string is good if there are no repeated characters.
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.

from collections import Counter

class Solution:

    def countGoodSubstrings(self, s):

        '''
        :param s:
        :return: return number of good substrings
        '''

        # Edge cases:
        # can it have only letters? characters are allowed. are they all of type char?
        # Is input length greater than or less than 3?
        # If no good strings then what do we return?
        # What if the input is empty?
        # xyzx
        #  | |  = 2.
        # this won't work as what if the letter occured after lp, so keep a hash map.
        count_substr = Counter(s[:3])
        num_good_strs = 1 if len(count_substr) == 3 else 0
        # Big O. O(len(s)) time | O(len(s)) space.
        for up in range(3, len(s)):
            if count_substr[up-3]:
                count_substr[s[up-3]] -= 1
            if count_substr[up-3] == 0:
                count_substr.pop(s[up-3])
            count_substr[s[up]] += 1
            num_good_strs += 1 if len(count_substr) == 3 else 0

        return num_good_strs

if __name__ == "__main__":
    sol = Solution()
    assert ( sol.countGoodSubstrings("xyz") == 1)
    assert (sol.countGoodSubstrings("xyzz") == 1)
    assert (sol.countGoodSubstrings("xyza") == 2)
    assert ( sol.countGoodSubstrings("") == 0 )
    # call function Here.
