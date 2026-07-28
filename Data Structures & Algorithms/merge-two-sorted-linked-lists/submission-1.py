# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ret = ListNode(-1, None)
        cur = ret

        l1, l2 = list1, list2

        while l1 or l2:

            if l2 and not l1:
                take = l2
            elif l1 and not l2:
                take = l1
            else:
                take = l1 if l1.val <= l2.val else l2

            new = ListNode(take.val, None)
            cur.next = new
            cur = cur.next

            if take == l1:
                l1 = l1.next
            else:
                l2 = l2.next

        return ret.next