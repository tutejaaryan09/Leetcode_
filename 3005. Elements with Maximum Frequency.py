class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans={}
        for i in nums:
            ans[i]=ans.get(i,0)+1
        res = dict(sorted(ans.items(), key=lambda item: item[1],reverse=True))
        maxi = list(res.values())[0]
        num=0
        for i,j in res.items():
            if j==maxi:
                num+=j
        return num