class solution:
    def printnum(self,i,n):
        if i>n:
            return
        print(i)
        self.printnum(i+1,n)
if __name__=="__main__":
    sol=solution()
    n=5
    sol.printnum(1,5)