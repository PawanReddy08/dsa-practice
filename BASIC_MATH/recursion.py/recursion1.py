class solution:
    def printName(self,name,count,n):
        if count==n:
            return
        print(name)
        self.printName(name,count+1,n)
if __name__=="__main__":
    sol=solution()
    n=5
    name="pawan"
    sol.printName(name,0,n)