class Solution:
    def pattern3(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
            for j in range(2*i+1):
                print("*",end="")
            for j in range(n-i-1):
                print(" ",end="")
            print()
if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern3(n)