class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = {}

        for s in strs:
            tmp = sorted(s)
            sn = "".join(tmp)

            if sn in mp:
                mp[sn].append(s)
            else:
                mp[sn] = [s]
        
        return list(mp.values())