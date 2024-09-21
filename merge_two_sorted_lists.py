def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    i = 0
    j = 0

    len_1 = len(list1)
    len_2 = len(list2)


    res = []

    while i < len_1 and j < len_2:
        if list_1[i] <= list_2[j]:
            res.append(list_1[i])
            i+=1 
        else:
            res.append(list_2[j])
            j+=1

        
    if i<len_1:
        res+= list_2[j:]
    else:
        res+= list_1[i:]