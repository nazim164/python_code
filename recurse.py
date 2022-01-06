# def Facto(num):
#     if num==1:
#         return 1
#     else:
#         return (num*Facto(num-1))
    
# def Main():
#     num=int(input("Enter A Number :"))
#     print("Factorial Of ",num,"Is :",Facto(num))
    
# if __name__=="__main__":
#     Main()
    

# def Multi(n,x):
#     if x==0:
#         return
#     else:
#         print(n," * ",(11-x)," = ",n*(11-x))
        
#     x-=1
#     Multi(n,x)
# def Main():
#     n=int(input("Enter A Number :"))
#     Multi(n,10)
# if __name__=="__main__":
#     Main()
    
# def Fibbo(ft,st,tt):
#     if tt==2:
#         return
#     else:
#         rt=ft+st
#         print("",rt,end="")
#         ft=st
#         st=rt
#     tt-=1
#     Fibbo(ft,st,tt)
    
# def Main():
#     ft=int(input("Enter First Number :"))
#     st=int(input("Enter Second Term  :"))
#     tt=int(input("Enter Total Term :"))
#     print(ft,"",st,end="")
#     Fibbo(ft,st,tt)
    
# if __name__=="__main__":
#     Main()
    
    
def Summ(n,sum):
    if n>100:
        print("Summation",sum)
        return
    else:
        print(n)
        sum+=n
    n+=2
    Summ(n,sum)
n=0
sum=0
Summ(n,sum)
    
    