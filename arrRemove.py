import array

arr=array.array('i',[1,2,3,4,5,6])
print("Before removing The Element In The Array")
for i in range(0,6):
    print(arr[i])

arr.pop(2)
print("After The removing The Element In The Array ")
for i in range(0,6):
    print(arr[i])