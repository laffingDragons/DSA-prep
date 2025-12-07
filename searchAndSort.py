#linear search


from typing import Any


from turtle import right


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

#bubble sort with break if all the elements are sorted
def swap(a,b):
    temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
    

def bubbleSort(n = len(arr)):
    isSwapped = False;
    for i in range(n):
        for j in range(n-1-i):
            if(arr[j] > arr[j+1]):
                swap(j, j+1)
                isSwapped = True;
        if not isSwapped:
            break;
    return arr;                

# print("Bubble sorted array is : ",bubbleSort())

#Selection sort means Select the minimum and put it in front
# def selectSort():
#     for i in range(len(arr)):
#         min = arr[i];
#         print(arr[i+1], min)
#         if(arr[i+1] < min):
#             min = arr[i]
            
#         arr[i] = min;
#     return arr
# print("Select sorted array is : ",selectSort())

#Insertion sort code comes here


#Use merge sort to sort an array
arr2 = [5, 1, 6, 4, 2, 3];

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergeSort(mergeArr):
    if len(mergeArr) <= 1:
        return mergeArr
    mid = len(mergeArr) // 2
    left = mergeSort(mergeArr[:mid])
    right = mergeSort(mergeArr[mid:])
    return merge(left, right)


print("The merge sorted array is:", mergeSort(arr2))
