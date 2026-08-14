class Solution:
    def pattern2(self, n):
        for i in range(n):
            print("* "*(i+1))
if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern2(n)