 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def hasCycle(self, head: ListNode) -> bool:
    
        # Solution 1 
        # * Make a seen set and add nodes that are seen to keep track of them
        # * If you see a node that is in the set, then return True. 
        # * If no such node exists until the end of list exit the loop & return False 
        # * Big O. O(n) time | O(n) space
        
        seen = set()
        
        while head:
            
            if head in seen: 
                return True 
            seen.add(head)
            head = head.next 
            
        return False  
    
        # Solution 2 
        # * Initialize two pointers.    
        # * Make one go twice as fast as the other. 
        # * If both of them are equal before the slow pointer hits the end, 
        #   then there is a cycle. This should be true because at the start 
        #   1 -> 2 -> 3 . The faster runner takes half the time to cover the same                     ^    *        distance as the slow runner.    
        #  n-1 hoops. (n-1)//2 
        

        if head is None or head.next is None: 
            return False 
        sp = head 
        fp = head.next 
        
        while fp is not None and fp.next is not None: 
        #while sp is not None: 
            if (fp == sp): 
                return True 
            fp = fp.next.next 
            sp = sp.next 
        return False 


