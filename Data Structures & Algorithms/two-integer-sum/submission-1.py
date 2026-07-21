class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)): #these are list indexes
            for y in range(x+1, len(nums)): #these are list indexes
                if nums[x] + nums[y] == target:
                    return [x,y]
        return []