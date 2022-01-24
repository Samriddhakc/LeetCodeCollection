
from collections import  deque
from collections import defaultdict

class Solution:

    def canFinish( self, numCourses, prerequisties ):

        '''
        :param prerequisties:
        :return:
        '''

        # if numCourses > len(prerequisties): # if num courses greates than prereq, then you can take each course individually.
        #     return True
        #
        # if numCourses < len(prerequisties): # If numcourses to take less than prereq cannot do this.
        #     return False

        in_deg = defaultdict(int)
        graph = defaultdict(list)

        for course in prerequisties:
            in_deg[course[1]] += 1
            graph[course[0]].append(course[1])

        queue = deque([])

        for key in range(numCourses):
            if in_deg[key] == 0:
                queue.append(key)

        count = 0
        while queue:
            curr_course = queue.popleft()
            count += 1
            for neigh in graph[curr_course]:
                in_deg[neigh] -= 1
                if in_deg[neigh] == 0:
                    queue.append(neigh)

        return count == numCourses



if __name__ == "__main__":

    sol = Solution()
    assert ( sol.canFinish(10, []) == True )
    assert ( sol.canFinish(0, []) == True )
    assert ( sol.canFinish(0, [[1, 0]]) == True )
    assert ( sol.canFinish(2, [[1, 0]]) == True )
    assert ( sol.canFinish(3, [ [0, 1],[0, 2], [1, 3] ]) == False )
    assert ( sol.canFinish(4, [ [0, 1],[0, 2], [1, 3] ]) == True )


