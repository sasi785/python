arr=[10,40,50,70,90]
max=arr[0]
for i in range(0,len(arr)):
    if(arr[i]>max):
        max=arr[i]
print("The largest element in array:"+str(max))
