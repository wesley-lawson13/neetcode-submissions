class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        print(freqs)

        buckets = [[] for _ in range(len(nums))]
        print(buckets)
        for num in freqs:
            buckets[freqs[num]-1].append(num)
            
        res = []
        for i in range(len(nums)-1, -1, -1):

            if len(buckets[i]) > 0:

                for num in buckets[i]:

                    res.append(num)

                    if len(res) == k:
                        return res
        
        return res
                    
