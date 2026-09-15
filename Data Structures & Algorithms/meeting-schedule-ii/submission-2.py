"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        min_heap = []
        intervals.sort(key = lambda i : i.start)
        
        conflicts = 0
        for i in intervals:
            
            while min_heap and i.start >= min_heap[0]:
                heapq.heappop(min_heap)
            
            if not min_heap or i.start < min_heap[0]:
                heapq.heappush(min_heap, i.end)
            
            conflicts = max(len(min_heap), conflicts)
            
        return conflicts

            

            

        