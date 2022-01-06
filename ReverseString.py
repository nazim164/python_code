def display(n):
    cal=n.split(' ')
    show=''.join(reversed(cal))
    return show
if __name__=="__main__":
    str=input("Enter A String :")
    print(display(str))
    