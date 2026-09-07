import string
class Solution():
    def pattern14(self,n):
        letters=string.ascii_uppercase
        for i in range(n):
            print(letters[:i+1])
        print()
if __name__ == "__main__":
    sol=Solution()
    n=5
    sol.pattern14(n)
