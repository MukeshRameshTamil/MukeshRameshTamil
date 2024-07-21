class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_length = len(nums)
       
        i = 0

       
        while i < nums_length:

            val_at_i = nums[i] - 1

           
            belongs_in_range = 0 <= val_at_i < nums_length

            if belongs_in_range and nums[i] != nums[val_at_i]:
                nums[i], nums[val_at_i] = nums[val_at_i], nums[i]
            else:
                i += 1

      
        for x in range(nums_length):
           
            if x + 1 != nums[x]:
                return x + 1

       
        return nums_length + 1
