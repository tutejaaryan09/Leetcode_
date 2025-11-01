class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n=len(arr)
        ans={}
        for i in arr:
            ans[i]=ans.get(i,0)+1
        res = dict(sorted(ans.items(), key=lambda item: item[1], reverse=True))
        for i,j in res.items():
            if i==j:
                return i
        return -1