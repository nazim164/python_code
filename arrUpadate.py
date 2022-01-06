import array

arr=array.array('i',[1,2,3,4,5,6,7])
print("Before Updating The Array")
for i in range(0,6):
    print(arr[i])
    
arr[3]=8 
print("After Updating The Array :")
for i in range(0,6):
    print(arr[i])