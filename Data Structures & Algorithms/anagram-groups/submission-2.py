class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for s in strs:
            freq_list = [0 for _ in range(26)]
            for char in s:
                freq_list[ord(char) - ord('a')] += 1

            mp[tuple(freq_list)].append(s)

        return list(mp.values())