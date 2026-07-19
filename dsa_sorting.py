#bubble sort
arr=[7,3,4,2,8,1,9]
n=len(arr)
for i in range (n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

#insertion sort
arr=[10,4,2,8,3,9,5]
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>arr[j+1]:
        arr[j+1]=arr[j]
        j-=1
        arr[j+1]=key
print(arr)

#selection sort
arr=[37,12,98,56,73]
n=len(arr)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr) 
