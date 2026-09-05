class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        ret = []
        path = []
        seen = set()

        def dfs(i):
            if i == len(nums):
                new = sorted(path.copy())
                key = ','.join(str(num) for num in new)
                if key not in seen:
                    ret.append(path.copy())
                    seen.add(key)
                return

            path.append(nums[i])
            dfs(i+1)

            path.pop()
            dfs(i+1)

        dfs(0)
        return ret