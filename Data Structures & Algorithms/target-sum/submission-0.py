class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum=sum(nums)
        if (total_sum+target)%2!=0:
            return 0
        if (total_sum+target)<0:
            return 0
        positive_group=(total_sum+target)//2
        dp=[0]*(positive_group+1)
        dp[0]=1
        for num in nums:
            for j in range(positive_group,num-1,-1):
                dp[j]+=dp[j-num]
        return dp[positive_group]