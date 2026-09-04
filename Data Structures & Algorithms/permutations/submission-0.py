class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        path = []

        def bt(nums_set):

            if not nums_set:
                ret.append(path.copy())
                return

            for num in nums_set:
                path.append(num)
                new = nums_set.copy()
                new.remove(num)
                bt(new)
                path.pop()

        bt(set(nums))
        return ret