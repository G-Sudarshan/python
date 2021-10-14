# A peak element in an array is the one that is not
# smaller than its neighbours.
# Given an array arr[] of size N, find the index of any
# one of its peak elements.
n =int(input("Size: "))
arr = list(map(int,input("Array: ").strip().split()))[:n]
f=0
if n==1:
    print("Peack element",arr[0],"found at arr[",0,"]")
    f=1
else:
    for i in range(n):
        if(i==0):
            if arr[i] >= arr[i+1]:
                print("Peack element",arr[i],"found at arr[",i,"]")
                f=1
                break
        elif i>0 and i< n-1:
            if arr[i-1] <= arr[i] >= arr[i+1]:
                print("Peack element",arr[i],"found at arr[",i,"]")
                f = 1
                break
        elif i == n-1:
            if arr[i] >= arr[i-1]:
                print("Peack element",arr[i],"found at arr[",i,"]")
                f = 1
                break
if f == 0: print("No Peack element")


