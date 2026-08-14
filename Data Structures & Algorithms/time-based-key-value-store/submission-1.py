class TimeMap:

    def __init__(self):
        self.m = {} # str : [(str,int),(str,int)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""

        elements = self.m[key]
        l = 0
        r = len(elements) - 1
        ans = ""

        while l <= r:
            m_index = (l+r)//2
            m = elements[m_index]
            m_val = m[0]
            m_time = m[1]
        
            if timestamp == m_time:
                return m_val
            
            if m_time < timestamp:
                ans = m_val
                l = m_index + 1
            else:
                r = m_index - 1
                
        return ans
                




        
