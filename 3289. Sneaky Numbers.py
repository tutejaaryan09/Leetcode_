class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans={}
        res=[]
        for i in nums:
            ans[i]=ans.get(i,0)+1

        for i,j in ans.items():
            if j==2:
                res.append(i)
        return res
