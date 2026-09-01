class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)
        
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        q = deque() # having values (ready_time, count)

        time = 1
        while q or max_heap:
            time += 1
            if q and q[0][0] == time:
                _, count = q.popleft()
                heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1

                if count < 0:
                    q.append((time + n + 1, count))
            

        return time-1