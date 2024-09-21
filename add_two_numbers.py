from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # iterate over both, add numbers, if over ten use extra one for next step, sum is modulo 10
    # if both are the same length
    ## extra one 0 -> done
    ## extra one 1 -> add node wid value 1
    # if both are not same length
    ## use sequence that has self.next != Null and add one, repeat same Logic for adding 

    # two parts
    ## when both have elements
    ## I only have element that has values

    sum_list1 = l1
    sum_list2 = l2
    tmp_sum = sum_list1.val + sum_list2.val
    uebertrag = tmp_sum >= 10
    result = ListNode(tmp_sum %10)
    sum_list1 = sum_list1.next
    sum_list2 = sum_list2.next

    while sum_list1 or sum_list2:
        summand1 = sum_list1.val if sum_list1 else 0 
        summand2 = sum_list2.val if sum_list2 else 0 

        sum_tmp = summand1 + summand2
        new_res = ListNode()
        new_res.val = sum_tmp % 10 + uebertrag
        uebertrag = sum_tmp >= 10

        result.next = new_res
        result = new_res
        sum_list1 = sum_list1.next
        sum_list2 = sum_list2.next


    return result