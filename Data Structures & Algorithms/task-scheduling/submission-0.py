class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = {}

        for char in tasks:
            counts[char] = counts.get(char, 0) + 1

        max_heap = []
        for key in counts:
            max_heap.append(-counts[key])

        heapq.heapify(max_heap)

        time = 1
        q = deque()
        while max_heap or q:
            while q and q[0][1] == time:
                count, _ = q.popleft()
                heapq.heappush(max_heap, count)
            
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1

                if count < 0:
                    q.append([count, time + n + 1])

            if not q and not max_heap:
                return time
            
            time += 1



    