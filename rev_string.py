# str=input("Enter String :")
# print("Original String Is :",str)
# str1=str[::-1]
# print("Reverse String Is :",str1)

# str=input("Enter String :")
# print("Original String Is =>",str)
# print("Change String To Upper Case :",str.upper())
# print("Change String To Lower Case :",str.lower())

# str=input("Enter String :")
# newstr=''
# cnt1=0
# cnt2=0
# cnt3=0

# for a in str:
#     if (a.isupper())==True:
#         cnt1+=1
#         newstr+=(a.lower())
#     elif (a.islower())==True:
#         cnt2+=1
#         newstr+=(a.upper())
#     elif (a.isspace())==True:
#         cnt3+=1
#         newstr+=a
        
# print("Original String Is :",str)
# print("UpperCase Is :",cnt1)
# print("LowerCase Is :",cnt2)
# print("White Space Is :",cnt3)

# print("Changing The String")
# print(newstr)

# str=input("Enter String :")
# vcnt=0
# ccnt=0
# for ch in str:
#     if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
#         vcnt+=1
#     else:
#         ccnt+=1
        
# print("Number Of Vowels Is :",vcnt)
# print("Number Of Consonant Is :",ccnt)

# str1=input("Enter First String :")
# str2=input("Enter Second String :")
# str3=input("Enter Thhird String :")

# print("Concate Of Three String Is :",str1+str2+str3)

str=input("Enter String :")

print("First Position Element In String :",str[0])
print("Second Position Element In String :",str[1])
print("Slicing",str[0:4])
print("Slicing :",str[1:-2])
