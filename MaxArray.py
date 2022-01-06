def Show(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max
arr=[10,35,85,45,69,96]
n=len(arr)
f1=Show(arr,n)
print("List Of Array Is :",f1)
    
