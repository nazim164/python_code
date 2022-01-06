#demo NameError

# try:
#     print(x)
# except NameError:
#     print("X Is Not Defined")
    
# except:
#     print("something went wrong")


# Demo DivideByZero

# x=0
# try:
#     print("Divided By Zero Exception")
# except:
#     print("Something Went Wrong")
# finally:
#     print("Value Of X Is :",x)
    
# Demo raise
# x=-1
# if x<0:
#     raise Exception("Sorry,No Number Below Zero")

# Demonstrating raise 
x="hello"
if not type(x) is int:
    raise TypeError("Only Integer Are Allowed")

print("Value Of x Is:",x)


