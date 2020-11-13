# Code Path Prep Question 1. Delete Node in a linked list
# Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list

class ListNode: 

    def __init__(self,x=0): 
        self.val = x
        self.next = None  

    def prin(self):
        head = self.next 
        while head and head.next: 
            print(head.val, end= "->") 
            head=head.next 
        print(head.val)


class Solution: 
    
    def deleteNode(self, node): 
        
        # If the tail is not the last node, we next node.next is not null. Hence, copy node.next to be node. 
        # O(1) time | O(1) space 

        node.val = node.next.val 
        node.next = node.next.next 






def main(): 

    sol = Solution() 
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    # testcase1 
    dummyHead = ListNode()
    dummyHead.next = node1 
    node1.next = node2 
    dummyHead.prin()
    sol.deleteNode(node1)
    dummyHead.prin()

main()