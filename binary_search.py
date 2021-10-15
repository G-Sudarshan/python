# Faster searching algorithm for sorted array.
# By Ratan Raj Ojha

def bin_search( arr, num):
    min=0
    max=len(arr)-1
    mid=0
    while(min<=max):
        mid=(min+max)//2
        if(num>arr[mid]):
            min=mid+1
        elif(num<arr[mid]):
            max=mid-1
        else:
            return mid
    return -1
    

arr = [10, 15, 22, 26, 27, 34, 40, 52, 68, 80, 81, 87, 88, 98, 99, 100] #array must be sorted
num = 68 #number to be searched
ans = bin_search(arr,num)
if(ans != -1):
    print("{} found at {} index.".format(num,ans))
else:
    print("Number not found.")
