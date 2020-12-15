class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Solution 1 
        # * Initialze a result linked list called ListNode()
        # * Assign a dummy_head to result linked_list. 
        # * If l1 and l2 is not None, if l1.val > l2.val then assign result.next =                       ListNode(l2.val) l2.next else assign to ListNode(l1.val) l1.next 
        #  update l1 = l1.next, l2 = l2.next, result = result.next 
        #  result = result.next 
        # return dummy_head.next 
        # Big O. O(min(l1,l2)) time | O(min(l1,l2)) space 
        # To optimize space, don't get a new list result.caclulate length and chose just inrialize a dummy head and without assigning new space assign new pointers. O(1) time 
        
        result = ListNode()
        dummy_head = result 
        while l1 and l2: 
            if l1.val > l2.val: 
                result.next = l2 
                l2 = l2.next 
            else: 
                result.next = l1
                l1 = l1.next
            result = result.next
        if l1: 
            result.next = l1
        if l2: 
            result.next = l2
        
        return dummy_head.next 