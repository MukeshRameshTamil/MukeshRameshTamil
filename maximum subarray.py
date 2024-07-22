class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # Initialize to the smallest possible value
        current_sum = 0  # Variable to keep track of the current subarray sum
        
        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0 
        
        return max_sum 
