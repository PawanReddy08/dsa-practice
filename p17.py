import string
class Solution:
    def pattern17(self,n):
        # letter=string.ascii_uppercase
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
            for j in range(i+1):
                print(j,end="")
            for j in range(i-1,-1,-1):
                print(j,end="")
            for j in range(n-i-1):
                print(" ",end="")
            print()
if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern17(n)