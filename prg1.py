def f1(n):
    f=1
    while(n>0):
        f*=n
        n-=1
    return f
def f2():
    n=int(input("Enter A Number :"))
    print(n,"Factorial Is :",f1(n))
if __name__=="__main__":
    f2()
 
    