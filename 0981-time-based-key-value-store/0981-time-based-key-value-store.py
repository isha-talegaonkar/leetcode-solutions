class TimeMap:

    def __init__(self):
        self.keyValueStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.keyValueStore:
            self.keyValueStore[key] = []
        
        self.keyValueStore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.keyValueStore:
            return ""
        
        left = 0
        right = len(self.keyValueStore[key])
        
        while left < right:
            mid = left + (right - left) // 2
            
            if self.keyValueStore[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        return "" if right == 0 else self.keyValueStore[key][right-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)