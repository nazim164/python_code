import array

arr=array.array('i',[1,2,3])
print("Before Inserting The Array  :")
for i in range(0,3):
    print(arr[i])
    
arr.insert(1,8)
print("After The Insertion Element In The Array :")
for i in range(0,3):
    print(arr[i])
    
    
# insert element in float value

