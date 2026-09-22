class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums): 
            return True #if there are duplicates
            
        else:
            return False