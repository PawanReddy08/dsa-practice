class solution():
    def palindrome(self,n):
        dup=n
        rev=0
        while n>0:
            ld=n%10
            rev=(rev*10)+ld
            n=n//10
        if dup==rev:
            return True
        else:
            return False
obj=solution()
n=121
print(obj.palindrome(n))