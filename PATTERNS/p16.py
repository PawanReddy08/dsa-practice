import string
class Solution:
    def pattern16(self,n):
        letter=string.ascii_uppercase
        for i in range(n):
            print(letter[i]*(i+1))
        print()
if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern16(n)
