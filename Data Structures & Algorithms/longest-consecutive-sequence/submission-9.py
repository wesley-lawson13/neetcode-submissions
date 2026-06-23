class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)

        longest = 0
        for num in nums:
            if num-1 not in num_set:
                cur = 1
                while num+1 in num_set:
                    num += 1
                    cur += 1
            
                longest = max(cur, longest)
        
        return longest
                
