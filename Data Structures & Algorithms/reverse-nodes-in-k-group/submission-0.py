# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        right = dummy
        start = head
        last = dummy # the last 'end' value to be pointer at the next, starts with dummy

        while True:
            count = k
            while count > 0:
                
                right = right.next
                if not right:
                    return dummy.next
                count -= 1
            
            tmp = right.next # hold bc the reverse changes it
            self.reverse(start, k)
            # start becomes the back: set start.next to the tmp
            start.next = tmp
            last.next = right
            right = start
            last = right
            start = start.next            
    
    def reverse(self, start: Optional[ListNode], count: int) -> Optional[ListNode]:

        prev = None
        cur = start
        while count > 0:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            count -= 1