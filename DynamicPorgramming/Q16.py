class Solution:
    def numSplits(self, s: str) -> int:

        # good_ways = 0
        # for i in range(len(s) + 1):
        #     if  len(set(s[:i])) == len(set(s[i:])) :
        #            good_ways += 1
        # return good_ways

        # Big O(len(s)) time | O(len(s)) space

        hash_left = [0] * (len(s) + 1)  # number of unique strings upto idx.
        hash_right = [0] * (len(s) + 1)
        l_set, r_set = set(), set()
        n = len(s)

        for idx in range(len(s)):

            if s[idx] not in l_set:
                hash_left[idx + 1] = hash_left[idx] + 1
                l_set.add(s[idx])
            else:
                hash_left[idx + 1] = hash_left[idx]

            if s[n - idx - 1] not in r_set:
                hash_right[n - idx - 1] = hash_right[n - idx] + 1
                r_set.add(s[n - idx - 1])
            else:
                hash_right[n - idx - 1] = hash_right[n - idx]

        count = 0
        hash_left = hash_left[1:]
        hash_right = hash_right[:-1]

        for idx in range(len(hash_left) - 1):
            if hash_left[idx] == hash_right[idx + 1]:
                count += 1

        return count
