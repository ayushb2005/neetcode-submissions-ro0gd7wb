class TimeMap:

    def __init__(self):
        self.map = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key in self.map):
            self.map[key].append([value, timestamp])
        else:
            self.map[key] = [[value, timestamp]]
        print(self.map)
    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.map):
            return ""
        keyArray = self.map[key]
        left = 0 
        right = len(keyArray)-1

        while(left <= right):
            middle = (left + right) // 2
            if(keyArray[middle][1] == timestamp):
                return keyArray[middle][0]
            elif(keyArray[middle][1] > timestamp ):
                right = middle - 1
            else:
                left = middle + 1
        if(timestamp < keyArray[right][1]):
            return ""
        return keyArray[right][0]
