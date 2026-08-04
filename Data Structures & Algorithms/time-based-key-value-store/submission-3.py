class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        
        self.mp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.mp:
            return ""
        
        values = self.mp[key]
        l, r = 0, len(values)
        res = ""
        while l < r:
            mid = (l + r) // 2

            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid

        return res


        
