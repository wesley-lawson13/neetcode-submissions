class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}
        ret = []
        for i, num in enumerate(nums):
            if num in mp:
                return [mp[num], i]
            
            leftover = target - num
            mp[leftover] = i

        
