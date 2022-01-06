def Smallest(arr,n):
    min=arr[1]
    for i in range(1,n):
        if arr[i]<min:
            min=arr[i]
    return min
arr=[10,15,12,1,90,25]
n=len(arr)
f3=Smallest(arr,n)
print("Smallest Lis Of Array Is :",f3)
        
    