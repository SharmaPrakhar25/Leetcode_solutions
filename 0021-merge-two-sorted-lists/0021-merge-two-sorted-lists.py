# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None

        while list1 and list2:
            if list1.val <= list2.val:
                if head is None:
                    head = list1
                else:
                    curr.next = list1
                list1 = list1.next
            else:
                if head is None:
                    head = list2
                else:
                    curr.next = list2
                list2 = list2.next

            if curr is None:
                curr = head
            else:
                curr = curr.next
        
        while list1:
            if curr:
                curr.next = list1
                curr = curr.next
            else:
                head = list1
                curr = head
            list1 = list1.next


        while list2:
            if curr:
                curr.next = list2
                curr = curr.next
            else:
                head = list2
                curr = head
            list2 = list2.next
            
        
        return head