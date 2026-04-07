class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        else:
            target=sum(nums)//2
            dp=[[False]*(target+1) for _ in range(len(nums)+1)]
            for i in range(len(nums)+1):
                dp[i][0]=True
            for i in range(1,len(nums)+1):
                for t in range(target+1):
                    #Skip
                    if nums[i-1]>t:
                        dp[i][t]=dp[i-1][t]
                    else:
                        dp[i][t]=dp[i-1][t] or dp[i-1][t-nums[i-1]] #Take it once
            return dp[len(nums)][target]