class TimeMap:

    def __init__(self):
        self.d: dict[str, tuple] = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(value, timestamp)]
        else:
            self.d[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        arr = self.d[key]
        l = 0
        r = len(self.d[key]) - 1
        while r >= l:
            m = (r + l) // 2
            if timestamp < arr[m][1]:
                r = m - 1
            elif timestamp > arr[m][1]:
                l = m + 1
            else:
                return arr[m][0]
        if r == - 1:    
            return ""
        else:
            return arr[r][0]
