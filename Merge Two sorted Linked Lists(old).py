class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        listPtr1 = list1
        listPtr2 = list2
       
        finList = ListNode()
        tail = finList

        while list1 and list2 :
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
               # print(newList[1])
            else:
                tail.next = list2
                list2 = list2.next
            tail =tail.next
        #print(newList[1])

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        

        return finList.next
