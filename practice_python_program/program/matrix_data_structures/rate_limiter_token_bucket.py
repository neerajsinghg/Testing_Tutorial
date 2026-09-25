"""
Rate Limiter (Token Bucket Algorithm) for API Automation Testing
Senior SDET Context: Controls outgoing API request bursts to prevent hitting HTTP 429 Too Many Requests errors.
"""

import time

class TokenBucketRateLimiter:
    def __init__(self, capacity: int = 5, fill_rate_per_sec: float = 1.0):
        self.capacity = capacity
        self.fill_rate = fill_rate_per_sec
        self.tokens = float(capacity)
        self.last_fill_time = time.time()

    def _refill(self):
        now = time.time()
        elapsed = now - self.last_fill_time
        self.tokens = min(self.capacity, self.tokens + elapsed * self.fill_rate)
        self.last_fill_time = now

    def allow_request(self) -> bool:
        self._refill()
        if self.tokens >= 1.0:
            self.tokens -= 1.0
            return True
        return False

if __name__ == "__main__":
    limiter = TokenBucketRateLimiter(capacity=3, fill_rate_per_sec=2.0)
    for i in range(1, 6):
        allowed = limiter.allow_request()
        print(f"API Request #{i}: Allowed = {allowed}")
        if not allowed:
            time.sleep(0.5)
