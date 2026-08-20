# class Solution:
#     def pattern19(self,n):
#         for i in range(n):
#             spaces=0
#             print("* "*(n-i)+" "*(spaces)+"* "*(n-i))
#             spaces+=2
#         for i in range(n):
#             spaces=2*n-2
#             print("* "*(i+1)+" "*(spaces)+"* "*(i+1))
#             spaces-=2
# if __name__ == "__main__":
#     sol=Solution()
#     n=5
#     sol.pattern19(n)
class Solution:
    def pattern(self, n):
        # Top half
        for i in range(n):
            print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))
        
        # Bottom half
        for i in range(n):
            print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern(n)
