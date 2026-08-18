import string
class Solution:
    def pattern15(self,n):
        letter=string.ascii_uppercase
        for j in range(n,0,-1):
            print(letter[:j])
        print()
if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern15(n)