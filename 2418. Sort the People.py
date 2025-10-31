from collections import OrderedDict
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans={}
        retr=[]
        for i in range(len(names)):
            ans[heights[i]]=names[i]
        sort_ans = OrderedDict(sorted(ans.items(),reverse=True))
        for i,j in sort_ans.items():
            retr.append(j)
        return retr
