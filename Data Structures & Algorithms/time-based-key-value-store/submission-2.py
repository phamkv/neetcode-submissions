class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        vals = self.store[key]
        l = 0
        r = len(vals) - 1
        while l <= r:
            mid = (l+r)//2
            print(r)
            if vals[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if r == -1:
            return ""
        return vals[r][1]
