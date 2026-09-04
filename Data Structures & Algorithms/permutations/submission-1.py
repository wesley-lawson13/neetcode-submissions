class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        path = []
        pick = [False] * len(nums)

        def bt(pick):

            if len(path) == len(nums):
                ret.append(path.copy())
                return

            for i in range(len(nums)):
                if not pick[i]:
                    path.append(nums[i])
                    pick[i] = True
                    bt(pick)
                    path.pop()
                    pick[i] = False

            
        bt(pick)
        return ret