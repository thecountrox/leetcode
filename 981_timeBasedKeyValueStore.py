class TimeMap:

    def __init__(self):
        self._hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._hash:
            self._hash[key] = []
        self._hash[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self._hash.get(key, [])
        l = 0
        r = len(values) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if values[mid][1] <= timestamp:
                l = mid +1
                res = values[mid][0]
            else:
                r = mid -1
        return res

