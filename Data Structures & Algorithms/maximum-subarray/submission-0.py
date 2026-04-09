class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mp=nums[0]
        cp=nums[0]
        for i in range(1,len(nums)):
            cp=max(cp+nums[i],nums[i])
            mp=max(mp,cp)
        return mp