class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        min_k = r
        while l <= r:

            mid = l + (r - l) // 2
            print(f"mid: {mid}")

            if mid == 47:
                print(f"l: {l}, r: {r}")

            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)

            if total_hours <= h:
                min_k = mid
                r = mid - 1
                print(f"updating k with {min_k}")
            else:
                l = mid + 1

        return min_k