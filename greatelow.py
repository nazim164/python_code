a1=int(input("Enter First Number :"))
a2=int(input("Enter Second Number :"))
a3=int(input("Enter Third Number :"))     
if a1>a2 and  a1>a3:
    print(a1,"Is Greatest")
elif a2>a1 and a2>a3:
    print(a2,"Is Greatest")
else:
    print(a3,"Is Greatest")
if a1<a2 and a1<a3:
    print(a1,"Is Lowest")
elif a2<a1 and a2<a3:
    print(a2,"Is Lowest")
else:
    print(a3,"Is Lowest")