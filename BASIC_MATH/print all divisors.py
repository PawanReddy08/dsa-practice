class solution():
    def all_divisors(self,n):
        for i in range(1,n):
            if n%i==0:
                print(i)
obj=solution()
n=144
obj.all_divisors(n)