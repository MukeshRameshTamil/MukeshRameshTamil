class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [10 ** 100] * len(nums)
        dp[0] = 0

        for i in range (len(nums)):
            num = nums[i]
            
            stop = min(i + num + 1, len(nums))
            for j in range(1, stop - i):
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]    
