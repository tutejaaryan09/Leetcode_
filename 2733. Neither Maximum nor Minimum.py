class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        mini=nums[0]
        maxi=nums[n-1]
        if n<3:
            return -1
        for i in range(n):
            if nums[i]<maxi and nums[i]>mini:
                return nums[i]
