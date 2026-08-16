# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        right = last = dummy
        start = head

        while True:

            count = k
            while count > 0:
                right = right.next
                if not right:
                    return dummy.next
                count -= 1

            startNext = right.next    
            self.reverse(start, k) #flips start and end
            start.next = startNext
            last.next = right
            right = last = start
            start = start.next
             
    def reverse(self, node, k):

        prev = None
        cur = node
        while k > 0:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            k -= 1