sname=input("Enter Student Name :")
rno=int(input("Enter Student Roll No :"))
s1=int(input("Enter First Subject Mark :"))
s2=int(input("Enter Second Subject Mark :"))
s3=int(input("Enter Third Subject Mark :"))
s4=int(input("Enter Fourth Subject Mark :"))
s5=int(input("Enter Fivth Subject Mark :"))

sum=s1+s2+s3+s4+s5
print("Summation Of All Subject Is :",sum)
per=sum/5
print("Average Marks Of Student Is :",per)

if s1>40 and s2>40 and s3>40 and s4>40 and s5>40:
    result="Pass"
    print(result)
else:
    result="Fail"
    print(result)
if per<50 and result=="Fail":
    Grade="****"
    print(Grade)
elif per>50 and per<65 and result=="Pass":
    Grade="C"
    print(Grade)
elif per>65 and per<75 and result=="Pass":
    Grade="B"
    print(Grade)
elif per>75 and per<85 and result=="Pass":
    Grade="A"
    print(Grade)
elif per>85 and per<95 and result=="Pass":
    Grade="A+"
    print(Grade)
    
