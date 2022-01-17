
class Soluiton:

    def threeSum( self, nums ):

        '''
        :param nums:
        :return:
        '''
        if len(nums) <= 2:
            return []

        triplets = []

        # store the idx for each occurence of a number
        num_hash = {}

        seen_triplet = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                triplet = [-(nums[i] + nums[j]), nums[i], nums[j]]
                if -(nums[i] + nums[j]) in num_hash:
                    if (min(triplet), max(triplet)) not in seen_triplet:
                        triplets.append(triplet)
                        seen_triplet.add((min(triplet), max(triplet)))

            num_hash[nums[i]] = i

        return triplets

    # for i in range( len(nums) ):
        #     for j in range ( i + 1, len(nums) ):
        #         for k in range( j + 1, len(nums) ):
        #             if ( ( nums[i] + nums[j] + nums[k] ) == 0 ):
        #                 triplets.append( [ i, j, k] )
        #
        # return triplets

if __name__ == "__main__":
    sol = Soluiton()
    assert ( sol.threeSum([]) == [] )
    assert ( sol.threeSum([1]) == [] )
    assert ( sol.threeSum([1, 2]) == [] )
    assert ( sol.threeSum([0]) == [] )
    assert ( sol.threeSum([1, 2, 3, -3]) == [ [1, 2, -3] ] )
    assert ( sol.threeSum([1, 2, 3, -3, 0]) == [ [1, 2, -3], [3, -3, 0 ] ] )
    assert ( sol.threeSum([1, 2, 3, -3, 0, 3]) == [ [1, 2, -3], [3, -3, 0 ] ] )

