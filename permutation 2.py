class Solution(object):
    def permuteUnique(self, nums):
      
        l = permutations(nums)
        visited =[]
        for i in l:
            if i not in visited:
                visited.append(i)
        
        return visited
              
            
