class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_f, s2_f = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_f[ord(s1[i]) - ord('a')] += 1
            s2_f[ord(s2[i]) - ord('a')] += 1

        match = 0
        for i in range(26):
            match += 1 if s1_f[i] == s2_f[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            
            if match == 26: 
                return True

            # add right pointer to the freq map for s2, update matches
            index = ord(s2[r]) - ord('a')
            s2_f[index] += 1
            if s1_f[index] == s2_f[index]:
                match += 1
            elif s1_f[index] + 1 == s2_f[index]: 
                """ If s2 count goes over with this value,
                we need to decrement the match var """
                match -= 1

            # remove the left pointer val from s2 freq map and update match
            index = ord(s2[l]) - ord('a')
            s2_f[index] -= 1
            if s1_f[index] == s2_f[index]:
                match += 1
            elif s1_f[index] - 1 == s2_f[index]:
                """If the two were equal and the we just made them unequal 
                after removing the left pointer, we need to decrement match"""
                match -= 1
            l += 1

        return match == 26
            


            




        

        