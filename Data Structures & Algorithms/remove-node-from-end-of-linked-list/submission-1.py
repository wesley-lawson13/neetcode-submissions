# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = head
        total = 0

        while cur:
            cur = cur.next
            total += 1

        print(total)

        if total == 1:
            return

        pos = 0
        cur, prev = head, None

        while pos < total - n:
            prev = cur
            cur = cur.next
            pos += 1

        if pos == 0:
           head = head.next
        else: 
            prev.next = cur.next
        return head

        

