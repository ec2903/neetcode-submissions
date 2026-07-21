class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums)) #set removes the duplicates so if the length is different then it would return True/False
