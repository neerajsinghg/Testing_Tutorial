class LongestSubarraySumKbySlidingWindow:
        arr = [1, 2, 3, 1, 1, 1, 1]
        k = 3
        
        left = 0
        current_sum = 0
        max_len = 0
        start = 0
        end = 0
        
        for right in range(len(arr)):
            current_sum += arr[right]
        
            while current_sum > k:
                current_sum -= arr[left]
                left += 1
        
            if current_sum == k:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left
                    end = right
        
        print("Length:", max_len)
        print("Subarray:", arr[start:end+1])