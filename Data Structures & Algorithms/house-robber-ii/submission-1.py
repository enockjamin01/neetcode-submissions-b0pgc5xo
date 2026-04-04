class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        def hr(num):
            a=num[0]
            b=max(num[0],num[1])
            for i in range(2,len(num)):
                c=max(a+num[i],b)
                a=b
                b=c
            return b
        return max(hr(nums[1:n]),hr(nums[0:n-1]))

