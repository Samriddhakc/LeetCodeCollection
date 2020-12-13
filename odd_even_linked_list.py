class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        # Solution 1 
        # * Create an odd linked list and copy all the odd indexed elements here 
        # * Create an even linked list and copy all the even indexed elements here 
        # * Combine odd and even linked list by making odd point to the even
        # * Return the head of the odd linked list 
        # * O(n) time | O(n) space 
        
        '''odd_dummy_head = ListNode() 
        even_dummy_head  = ListNode()
        odd_pointer = odd_dummy_head
        even_pointer = even_dummy_head
        counter = 0 
        while head: 
            if (counter+1)%2 != 0: 
                odd_pointer.next = ListNode(head.val)
                odd_pointer = odd_pointer.next
            else: 
                even_pointer.next = ListNode(head.val)
                even_pointer = even_pointer.next
            counter += 1 
            head = head.next 
        odd_pointer.next = even_dummy_head.next
        return odd_dummy_head.next'''
    
        
        
        
        # A-->C--> B->C
        # |  |
        # op ep
        #  *********   **********
        #            ^            ^
        #            |            | 
        #            op           ep 
        #            nxop = op.next ; op.next  = ep.next 
        #            op.next.next = nxop 
        #            ep.next = ep.next.next 
        # Solution 2 
        # * Initialize an op as the pointer that points to the odd element
        # * Initialize an ep as the pointer that points to the even element  
        # * Make op point to the next odd element with the help of ep/ 
        #   to make the linked list consistent  op.next point to the correct element and 
        #   ep.next point to the correct element before the updates
        # * O(n) time | O(1) space 
        if head is None or head.next is None: 
            return head 
        op = head          
        ep = head.next
        while ep and ep.next: 
            opnx = op.next
            epnx = ep.next.next
            op.next = ep.next 
            op.next.next = opnx 
            ep.next = epnx
            ep = ep.next
            op = op.next
        return head 
    
       # op : 1 | 2
       # ep : 2 | 3
       # opnx: 2 | 3 
       # epnx: None 
        
       # 1 -> 2 -> 3 
       #  ^   ^
       # op    ep  (opnx = op.next, epnx = ep.next.next)
       # 1 -> 3  (op.next = ep.next)
       # 1 -> 3 -> 2 (op.next.next = opnx)
       # 1 -> 3 -> 2 -> None (ep.next = epnx)
       # ep = ep.next 
       # op = op.next
       # ********* *********
           