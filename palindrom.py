def display(n):
    return n==n[::-1]
n=input("Enter A String :")
f1=display(n)

if f1:
    print("String Is Palindrom")
else:
    print("String Is Not Palindrom")
    
    