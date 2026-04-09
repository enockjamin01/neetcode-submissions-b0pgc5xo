class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_max_jump=0
        for i in range(len(nums)):
            if i > current_max_jump:
                return False
            current_max_jump=max(current_max_jump,i+nums[i])
        return True