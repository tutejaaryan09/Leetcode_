class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i,num in enumerate(nums):
            c=target-num
            if c in ans:
                return [ans[c],i]
            ans[num]=i