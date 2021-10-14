#Given a sorted array arr[] of size N and an integer K.
# The task is to check if K is present in the array or not using ternary search.
# Ternary Search- It is a divide and conquer algorithm that can be used
# to find an element in an array. In this algorithm, we divide the
# given array into three parts and determine which has the key (searched element).


n = int(input("Array size: "))
arr = list(map(int,input("Array: ").strip().split()))[:n]
k = int(input("search element: "))
s=0;
l=n-1;
f=0;
while((l>=s) and (f==0)):
    m1 = int(s+ (l-s)/3)
    m2 = int(l-(l-s)/3)
    if arr[m1]==k:
        f=1
        print("Element found at arr[",m1,"].")
    elif arr[m2]==k:
        f=1
        print("Element found at arr[",m2,"].")
    elif k<arr[m1]:
        l = m1 - 1
    elif k>arr[m2]:
        s=m2 + 1
    else:
        s = m1 + 1
        l = m2 - 1
if f==0: print("Element Not found")