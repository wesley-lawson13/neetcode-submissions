class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        path = []
        taken = [False] * len(nums)

        def bt():

            if len(path) == len(nums):
                ret.append(path.copy())
                return

            for i in range(len(nums)):
                
                # take
                if not taken[i]:
                    taken[i] = True
                    path.append(nums[i])
                    bt()
                    path.pop()
                    taken[i] = False

        bt()
        return ret


                