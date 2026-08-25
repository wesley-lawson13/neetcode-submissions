class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        inverted = [-stone for stone in stones]

        # build inverted heap (s.t. max vals are at the top)
        heapq.heapify(inverted) 

        while len(inverted) > 1:

            x = heapq.heappop(inverted) * -1
            y = heapq.heappop(inverted) * -1

            if x > y:
                x, y = y, x

            if x == y:
                # don't add any of the stones back
                continue
            
            heapq.heappush(inverted, (y - x) * -1)

        return inverted[0] * -1 if inverted else 0
            


