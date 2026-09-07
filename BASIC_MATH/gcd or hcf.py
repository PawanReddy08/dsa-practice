class solution():
    def gcd(self,n1,n2):
        for i in range(1,min((n1,n2))):
            if n1%i==0 and n2%i==0:
                gcd=i
        print(gcd)
obj=solution()
n1=15
n2=20
obj.gcd(n1,n2)