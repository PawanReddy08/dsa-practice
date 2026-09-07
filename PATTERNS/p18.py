import string
class Solution:
    def pattern18(self,n):
        letter=string.ascii_uppercase
        for i in range(n):
            for j in range(i+1):
                print(letter[n-j-1],end="")
            print()
if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern18(n)
