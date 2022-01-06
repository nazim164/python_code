def display(n):
    r1=''.join(reversed(n))
    if(n==r1):
        return True
    return False
n=input("Enter A Number :")
sum=display(n)
if sum: 
    print("Number Is Plindrom")
else:
    print("Number Is Not Palindrom")
    