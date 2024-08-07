from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        min = t - 3000
        while self.requests[0] < min:
            self.requests.popleft()

        # for req in self.requests:
        #     if req >= min and req <= t:
        #         counter += 1
            
        return len(self.requests)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)