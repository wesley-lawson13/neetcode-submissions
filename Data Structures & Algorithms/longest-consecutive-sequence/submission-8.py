class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)

        count = 0
        for num in nums:

            val = num
            run = 1
            while val+1 in nums:
                run += 1
                val += 1

            count = max(run, count)

        return count