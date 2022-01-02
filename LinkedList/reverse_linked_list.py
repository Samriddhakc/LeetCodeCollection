
class Node: 

    def __init__(self, x, nx = None): 
        self.value = x
        self.next  = nx

    
    def __str__(self):

        st=""
        while self and self.next:
            st += str(self.value) + "->"
            self=self.next 
        st += str(self.value)
        return st 

    def __eq___(self,node): 

        while self or node:
            if self.val != node.val: 
                return False 
            node = node.next 
            self = self.next 
        return True 





class Solution: 
    
    def reverseList(self,head): 
        
        # Algorithm 1 
        # * Calculate the length of the list. Record the values in the list.   
        # * reverse the storage list. 
        # * Reconstruct the list from the storage list. 
        # * O(n) time | O(n) space
                
        # Algorithm 2
        # * Initialize prev to None, and curr = head & nx = head.next. curr.next = prev. curr=nx.  
        # * Big O, O(n) time | O(1) space

        curr, prev = head, None 
        while curr: 
            nx = curr.next 
            curr.next = prev 
            prev = curr
            curr = nx 
        return prev 

def main():

    sol = Solution()
    l1 = Node( 1, Node( 2 , None) )
    l2 = Node( 1, Node( 3 , None) )
    print(l1)
    l1_reverse = sol.reverseList(l1)
    print(l1_reverse)

main()