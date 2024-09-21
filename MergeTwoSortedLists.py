from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f"({self.val}, {self.next})"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        aux_node = ListNode()
        res = aux_node 
        if list1.val is None and list2.val is None:
            return ListNode()
        
        while l1.next is not None or l2.next is not None:
            if l1.val <= l2.val:
                aux_node.val = l1.val
                aux_node.next = ListNode()
                aux_node = aux_node.next
                l1 = l1.next
            else:
                aux_node.val = l2.val
                aux_node.next = ListNode()
                aux_node = aux_node.next
                l2 = l2.next
            
        if l1.next is None:
            aux_node.val = l1.val
            aux_node.next = l2
        else:
            aux_node.val = l2.val
            aux_node.next = l1
        return res

            
list1 = ListNode(1, ListNode( 2,ListNode(4))
) 
list2 = ListNode(1, ListNode( 3,ListNode(4))) 
# Output: [1,1,2,3,4,4]
sol = Solution()
print(sol.mergeTwoLists(list1=list1, list2=list2))