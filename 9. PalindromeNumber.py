class Solution:
    def isPalindrome(self, x: int) -> bool:
      x=str(x)
      n=str(x[::-1])
      for i in range(len(x)):
        if x[i]!=n[i]:
            return False
      return True
        