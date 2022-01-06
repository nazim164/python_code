def Arith(a,b):
    c=a+b
    print("Addtion Of Two Number Is :",c)
    c=a-b
    print("Substracttion Of Two Number Is :",c)
    c=a*b
    print("Multiplication Of Two Number Is :",c)
    c=a/b
    print("Division Of Two Number Is :",c)
    
def f1():
    a=int(input("Enter First Number :"))
    b=int(input("Enter Second Number :"))
    # c=int(input("Enter Third Number :"))
    Arith(a,b)
    
if __name__=="__main__":
    f1()
    
    