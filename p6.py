class Solution:
    def pattern6(self,n):
        for i in range(n):
            for j in range(n,i,-1):
                print(j,end=" ")
            print()
if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern6(n)