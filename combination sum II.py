class Solution:
    def __init__(self):
        self.result = []  # Resultant list to store combinations

   
    def solve(self, nums, target, index, lst):
        
        if target == 0:
            self.result.append(lst[:]) 
            return

       
        if index == len(nums) or target < nums[index]:
            return

        temp = nums[index]
        lst.append(nums[index]) 
        self.solve(nums, target - nums[index], index + 1, lst)  
        lst.pop() 

        i = 1
        while index + i < len(nums) and nums[index + i] == temp:
            i += 1  # Skip duplicates
        self.solve(nums, target, index + i, lst)  

   
    def combinationSum2(self, candidates, target):
        candidates.sort() 
        self.solve(candidates, target, 0, [])  # Call recursive function
        return self.result  
