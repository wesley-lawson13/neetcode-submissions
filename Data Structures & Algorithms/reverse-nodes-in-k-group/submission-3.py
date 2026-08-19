# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        start = head
        lastPrev = end = dummy

        while True:

            count = k
            while count > 0:
                end = end.next
                if not end:
                    return dummy.next
                count -= 1

            
            startNext = end.next
            self.reverse(start, k)
            # start now at the end, end at the start
            print(start.val)
            start.next = startNext
            lastPrev.next = end
            lastPrev = end = start
            start = start.next


    def reverse(self, start, k):

        prev = None
        while k > 0:
            tmp = start.next
            start.next = prev
            prev = start
            start = tmp
            k -= 1

