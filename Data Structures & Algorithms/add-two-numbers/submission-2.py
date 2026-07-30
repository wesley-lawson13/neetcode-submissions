# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, None)
        cur = dummy
        carry = 0
        
        while l1 or l2:

            if not l1 and l2:
                tot = l2.val + carry
                l2 = l2.next
            elif l1 and not l2:
                tot = l1.val + carry
                l1 = l1.next
            else:
                tot = l1.val + l2.val + carry
                l1, l2 = l1.next, l2.next
            
            digit = tot % 10
            carry = tot // 10

            new = ListNode(digit, None)
            cur.next = new
            cur = cur.next

            if carry == 1 and not (l1 or l2):
                cur.next = ListNode(1, None)

        return dummy.next
        

        

        

            

            




