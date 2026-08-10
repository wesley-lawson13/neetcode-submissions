# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists
        return lists[0]

    def merge(self, h1, h2):
        
        dummy = ListNode()
        cur = dummy

        while h1 and h2:
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        
        if h1:
            cur.next = h1
        else:
            cur.next = h2
        return dummy.next
            
            


                    
