#linear search


arr = [1, 4, 6, 7,9 , 0, 12];

def linerSearch(target):
    for i in range(len(arr)-1):
        if arr[i] == target: return i;

print("The target number has index of:",linerSearch(9))

# Binary Search
nums = [ -2 , -1, 0, 3, 4, 5, 7, 8, 10, 23, 45];

def binarySearch(target):
    left = 0;
    right = len(nums) - 1;
    
    while left <= right :
        
        middle = int((left + right) // 2)
        
        if(target == nums[middle]) : 
            return middle;
        if target > nums[middle]: 
            left = middle + 1;
        else:
            right = middle - 1;
    return -1;

print(binarySearch(45))

#bubble sort
def swap(a,b):
    temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
    
def bubbleSort(n = len(arr)):
    for i in range(n):
        for j in range(n-1-i):
            if(arr[j] > arr[j+1]):
                swap(j, j+1)
    return arr;                

print("Bubble sorted array is : ",bubbleSort())
