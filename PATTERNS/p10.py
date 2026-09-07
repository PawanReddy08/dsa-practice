class Solution:
    def pattern10(self,n):
        for i in range(1,2*n):
            if i<=n:
                print("* "*i)
            else:
                print("* "*(2*n-i))
if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern10(n)
