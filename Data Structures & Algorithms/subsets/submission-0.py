class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ret = []

        path = []
        def dfs_bt(i):
            
            if i >= len(nums):
                ret.append(path.copy()) # need to use copy because the path itself will be modified by pointer
                return

            # take nums[i]
            path.append(nums[i])
            dfs_bt(i+1)

            # do not take nums[i]
            path.pop()
            dfs_bt(i+1)

        dfs_bt(0)
        return ret
            


            

            

            
            

